#!/usr/bin/env python

import os
import urllib2
import sys
from subprocess import call

from settings import IMAGE_FILENAME
from scrape import get_random_image


def main():
    print "=== START ==="

    image_file_path = os.path.join('/Library/Desktop Pictures/', IMAGE_FILENAME)
    image_url = get_random_image()

    # Update desktop image & restart Dock
    if image_url is not None:
        print "Found image " + image_url
        print "Saving to " + image_file_path

        image_response = urllib2.urlopen(image_url)
        image_buffer = image_response.read()

        with open(image_file_path, 'wb') as image_file:
            image_file.write(image_buffer)

        image_response.close()

        call('killall Dock', shell=True)

        sys.exit(0)
    else:
        print "WARNING: No image was returned from scraper."


if __name__ == "__main__":
    main()
