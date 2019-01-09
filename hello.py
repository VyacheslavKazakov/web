#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hello(environ, start_response):
    args = environ['QUERY_STRING'].split('&')
    body = [bytes(i + '\n', 'ascii') for i in args]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body
