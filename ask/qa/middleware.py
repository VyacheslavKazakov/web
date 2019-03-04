#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

class CheckSessionMiddleware(class):
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
