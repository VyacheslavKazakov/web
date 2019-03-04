#!/usr/bin/python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import datetime

class CheckSessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        try:
            sessionid = request.COOKIE.get('sessionid')
            session = Session.objects.get(key=sessionid,
                                          expires__gt=datetime.now(),)
            request.session = session
            request.user = session.user
        except Session.DoesNotExist:
            request.session = None
            request.user = None
