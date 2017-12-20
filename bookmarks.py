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
from collections import OrderedDict

FIELDS = ['url','title','tags','options','notes']

def unpack(d):
    """ unpack dict """
    
    u = OrderedDict()
    
    for field in FIELDS:
        u[field] = d[field] if field in d else None

    return u    

def pack(u):
    """ pack dict, return only valid entries """
    
    return OrderedDict((k,v) for k,v in u.items() if v)
    
def represent_ordereddict(dumper, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

# make yaml dump ordered dict correctly
yaml.add_representer(OrderedDict, represent_ordereddict)

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
                
        return pack(self._data)
     
    
    def __getattr__(self,attr):
        
        if attr in self._data:
            return self._data[attr]
        
        
    def __repr__(self):
        return str(self._data)
    
    
    def updateTitle(self):
        """ get title from the site """
        r = requests.get(self.url)

        tree = fromstring(r.content)
        self._data['title'] = tree.findtext('.//title')
        
#

#%%


if __name__ == "__main__":


    dataDir = os.path.expanduser('~')+'/bookmarks'
    dbFile = os.path.join(dataDir,'bookmarks.yml')
    
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
        
    if not os.path.exists(dbFile):   
        b = Bookmark.from_dict( {'url':'https://www.example.com/'})
        b.updateTitle()
    
        data = {0:b.to_dict()}
        
        with open(dbFile,'w') as fid:
            yaml.dump(data,stream=fid,default_flow_style=False)
        
    # update titles
    
    data = yaml.load(open(dbFile,'r'))
    

