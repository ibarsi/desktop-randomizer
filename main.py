#!/usr/bin/env python

import os
import urllib
from subprocess import call

from settings import IMAGE_FILENAME
from scrape import get_random_image

image_file_path = os.path.join('/Library/Desktop Pictures/', IMAGE_FILENAME)

print get_random_image()

# # Update desktop image & restart Dock
# urllib.urlretrieve(get_random_image(), image_file_path)
# call(['killall', 'Dock'])
