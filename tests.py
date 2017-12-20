#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests for bookmark tool

@author: jev
"""
from bookmarks import Bookmark,unpack,pack

d = {'url':'http://www.example.com','title':'Test title','tags':'abc'}

def test_pacck_unpack():
    
    # test unpacking
    u = unpack(d)

    assert u['tags'] == d['tags']
    assert u['title'] == d['title']
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
    
def test_to_dict():
    
    b = Bookmark.from_dict(d)
    assert b.to_dict() == d
    
def test_attr():
    
    b = Bookmark.from_dict(d)
    assert b.url == d['url']
    
    assert b._data == unpack(d)
    
def test_update():
    
    b = Bookmark.from_dict(d)
    b.updateTitle()
    
    assert b.title == 'Example Domain'