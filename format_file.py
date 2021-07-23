#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import requests
import json
import time
import os
import subprocess

with open('/Users/lalitha.suggula/Downloads/files/sat_feb2apr_2021/feb2apr_2021_v.txt', 'r') as coverage_file:
    each_line=coverage_file.read()
    
print(len(each_line))
print(type(each_line))

date_set = set()
for i in each_line.split('\n'):
    each_item = i.split('\t')
    date = each_item[0].split('_')
    date_set.add(date[0])
print (date_set)

for date in date_set:
    print ("----each date is-----")
    print(date)
    #name = '2021-00-00'
    fp = open('Brazil_%s.csv' % date, 'w')
    fp.write("id,timestamp,wkt,sensor_type,published\n")
    #need to insert logic for end of file
    fp.close()
