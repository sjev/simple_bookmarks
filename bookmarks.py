#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bookmark manager

@author: jev
"""

import yaml
import requests
from lxml.html import fromstring
import os


FIELDS = ['url','title','tags','options','notes']

def unpack(d):
    """ unpack dict """
    
    u = {}
    
    for field in FIELDS:
        u[field] = d[field] if field in d else None

    return u    

def pack(u):
    """ pack dict, return only valid entries """
    
    return dict((k,v) for k,v in u.items() if v)
    
    

#%% 

class Bookmark():
    """ bookmark class """
    def __init__(self, **kwargs):
        
        
        assert 'url' in kwargs,  'Must provide bookmark url.'
        self._data = unpack(kwargs)
       
            
     
    
    @classmethod
    def from_dict(cls, data):
        """ 
        create class from dictionary 
        
        Parameters
        ------------
        data : dict
            data dictionary with keys url,title,tags,options. Only url is required
        """
        
        return cls(**data)
    
    def to_dict(self,full=False):
        """ convert to dictionary. """
        data = []
        
        for field in self._fields:
            val = getattr(self,field)
            if  val or full:
                if isinstance(val,list):
                    data.append((field,','.join(val)))
                else:
                    data.append((field,val))
        
        return dict(data)
     
    
    
    def updateTitle(self):
        """ get title from the site """
        r = requests.get(self.url)

        tree = fromstring(r.content)
        self.title = tree.findtext('.//title')
        
#

#%%

if __name__ == "__main__":


    dataDir = os.path.expanduser('~')+'/bookmarks'
    dbFile = os.path.join(dataDir,'bookmarks.yml')
    
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
        b = Bookmark.from_dict( {'url':'https://www.example.com/'})
        b.updateTitle()
    
        data = {0:b.to_dict()}
        
        with open(dbFile,'w') as fid:
            yaml.dump(data,stream=fid,default_flow_style=False)
        
    


