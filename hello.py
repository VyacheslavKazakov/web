#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hello(environ, start_response):
    args = environ['QUERY_STRING'].split('&')
    body = "\n".join(environ.get('QUERY_STRING').split("&"))
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body
