#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests for bookmark tool

@author: jev
"""
from bookmarks import Bookmark,unpack,pack

d = {'url':'http://www.example.com','title':'Example site','tags':'abc'}

def test_pacck_unpack():
    
    # test unpacking
    u = unpack(d)

    assert u['tags'] == 'abc'
    assert u['title'] == 'Example site'
    assert u['options'] == None
    assert u['notes'] == None

    # and packing
    p = pack(u)
    
    # result should now be original dict
    assert p==d


def test_from_dict():
    
    b = Bookmark.from_dict(d)
    
    
    assert b._data['tags'] == d['tags']
    assert b._data['url'] == d['url']
    assert b._data['notes'] == None