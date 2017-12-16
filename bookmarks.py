#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bookmark manager

@author: jev
"""

import yaml
import requests
from lxml.html import fromstring

dbFile = 'bookmarks.yml'

#%%
data = yaml.load(open(dbFile)) 

#%% test data
url = data[1]['url']
print(url)

r = requests.get(url)
print(r.status_code)

tree = fromstring(r.content)
title = tree.findtext('.//title')
print(title)

#%% write to disk
print(yaml.dump(data, default_flow_style=False))