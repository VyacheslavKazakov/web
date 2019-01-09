#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hello(environ, start_response):
    args = environ['QUERY_STRING'].split('&')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [print(i) for i in args]

bind = '0.0.0.0:8080'
pythonpath = "/home/box/web/"
