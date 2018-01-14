#!/usr/bin/env python

import os
import urllib
import sys
from subprocess import call

from settings import IMAGE_FILENAME
from scrape import get_random_image


def main():
    print "=== START ==="

    image_file_path = os.path.join('/Library/Desktop Pictures/', IMAGE_FILENAME)
    image = get_random_image()

    # Update desktop image & restart Dock
    if image is not None:
        print "Found image " + image

        urllib.urlretrieve(image, image_file_path)
        call('killall Dock', shell=True)

        sys.exit(0)
    else:
        print "WARNING: No image was returned from scraper."

if __name__ == "__main__":
    main()
