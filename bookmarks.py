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



#%% 

class Bookmark():
    """ bookmark class """
    def __init__(self, **kwargs):
        
        self._fields = ['url','title','tags','options']
        
        for field in self._fields:
            if field in kwargs:
                setattr(self,field,kwargs[field])
            else:
                setattr(self,field,None)
            
     
    
    @classmethod
    def from_dict(cls, data):
        """ 
        create class from dictionary 
        
        Parameters
        ------------
        data : dict
            data dictionary with keys url,title,tags,options. Only url is required
        """
        d = {}
        
        d['title'] = data['title'] if 'title' in data else ''
        
        
        for k in ['tags','options']:
            if k in data:
                d[k] = [field.strip() for field in data[k].split(',')]
        
        
        return cls(data['url'],**d)
    
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
        
#b = Bookmark.from_dict( {'url':'https://www.example.com/','options':'a,b,c'})
#
b = Bookmark(a=2,url='foo')
b.to_dict()

#%%


dataDir = os.path.expanduser('~')+'/bookmarks'
dbFile = os.path.join(dataDir,'bookmarks.yml')

if not os.path.exists(dataDir):
    os.mkdir(dataDir)
    b = Bookmark.from_dict( {'url':'https://www.example.com/'})
    b.updateTitle()

    data = {0:b.to_dict()}
    
    with open(dbFile,'w') as fid:
        yaml.dump(data,stream=fid,default_flow_style=False)
    



