#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from qa.models import Answer, Question, User, salt_and_hash

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def is_spam(self, text):
        return False

    def clean(self):
        if self.is_spam(self.cleaned_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def is_ethic(self, text):
        return True

    def clean_text(self):
        text = self.cleaned_data['text']
        if not self.is_ethic(text):
            raise forms.ValidationError(u'Сообщение некорректно', code=12)
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean_password(self):
        password = self.cleaned_data['password']
        hashed_password = salt_and_hash(password=password)
        return hashed_password

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user
