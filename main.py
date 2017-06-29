#!/usr/bin/env python

import os
import urllib
from subprocess import call

from settings import IMAGE_FILENAME
from scrape import get_random_image

image_file_path = os.path.join('/Library/Desktop Pictures/', IMAGE_FILENAME)

image = get_random_image()

# Update desktop image & restart Dock
if image is not None:
    urllib.urlretrieve(image, image_file_path)
    call('killall Dock', shell=True)
