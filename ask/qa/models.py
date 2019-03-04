#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import hashlib
import datetime
from datetime import timedelta
import string
import random

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_likes_user')
    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question_details', kwargs={'slug': self.id})

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question,null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'answers'

class User(models.Model):
    username = models.CharField(unique=True)
    password = models.CharField()
    email = models.CharField()

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'users'

class Session(models.Model):
    key = models.CharField(unique=True)
    user = models.ForeignKey(User)
    expires = models.DateTimeField()

def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None
    session = Session()
    session.key = generate_long_random_key()
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key

def salt_and_hash(password):
    m = hashlib.md5()
    salt = 'salt'
    return m.update(salt + password).hexdigest()

def generate_long_random_key():
    size=16
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))
