#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests for bookmark tool

@author: jev
"""
from bookmarks import Bookmark,unpack,pack,represent_ordereddict
import yaml
import os
import pytest
from collections import OrderedDict



d = {'url':'http://www.example.com','title':'Test title','tags':'abc'}
dataFile = 'data/bookmarks.yml'

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
    
    print(b.to_dict())
    
def test_attr():
    
    b = Bookmark.from_dict(d)
    assert b.url == d['url']
    
    assert b._data == unpack(d)
        

def test_load():
    """ load from db """
    
    
    data = yaml.load(open(dataFile,'r'))
    
    # create classes
    B = [Bookmark.from_dict(d) for d in data]    
    
    
    return B
    
def updateTitles(B):
    
    
    # update titles
    for b in B:
        b.updateTitle()
    
    assert B[0].title == 'Example Domain'
    
    return B

def test_save():
    """ save back to yml"""
    B = test_load()
    
    updateTitles(B)
    
    p,f = os.path.split(dataFile)
    n,e = os.path.splitext(f)
    dest = os.path.join(p,n+'_out'+e)
    
    data = [b.to_dict() for b in B]
    
    yaml.dump(data,open(dest,'w'),default_flow_style=False)