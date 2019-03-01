#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from qa.models import Answer

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def is_spam(text):
        return False

    def clean(self):
        if is_spam(self.cleaned_data):
            raise forms.ValidationError(u'Сообщение похоже на спам', code='spam')


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def is_ethic(text):
        return True

    def clean_text(self):
        text = self.cleaned_data['text']
        if not is_ethic(text):
            raise forms.ValidationError(u'Сообщение некорректно', code=12)
        return text + "\nYour question received."

    def save(self):
        post = Question(**self.cleaned_data)
        post.save()
        return post
