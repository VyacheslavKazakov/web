from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class qUser(User):

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'users'

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(qUser,null=False, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(qUser, related_name='question_likes_user')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/post/%d/' % self.pk

    class Meta:
        db_table = 'questions'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question,null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(qUser,null=False, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'answers'

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')
