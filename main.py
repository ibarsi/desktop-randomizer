#!/usr/bin/env python

import os
import json
import urllib
from subprocess import call

import scrape

with open('config.json') as config_file:
    config = json.load(config_file)

image_file_path = os.path.join('/Library/Desktop Pictures/', config['image_filename'])

# Update desktop image & restart Dock
urllib.urlretrieve(scrape.get_random_image(), image_file_path)
call(['killall', 'Dock'])
