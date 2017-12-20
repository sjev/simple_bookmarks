#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests for bookmark tool

@author: jev
"""
from bookmarks import Bookmark

d = {'url':'http://www.example.com','title':'Example site','tags':'abc'}

def test_from_dict():
    
    #b = Bookmark.from_dict(d)
    b = Bookmark.from_dict( {'url':'https://www.example.com/','options':'a,b,c'})
    print(b)