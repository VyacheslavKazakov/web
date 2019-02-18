from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    # id = models.SlugField(unique=True, primary_key=True)
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
        return "/question/{}/".format(self.id)

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']

class Answer(models.Model):
    # id = models.SlugField(unique=True, primary_key=True)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question,null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'answers'
