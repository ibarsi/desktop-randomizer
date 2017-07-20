from random import choice
from time import sleep

from lxml import html
import requests

from settings import IMAGE_URL, IMAGE_XPATH_FORMAT, IMAGE_START_VALUE, IMAGE_END_VALUE


def get_random_image():
    elements = extract_image_elements_from_url(IMAGE_URL, IMAGE_XPATH_FORMAT)

    if len(elements) == 0:
        print "WARNING: No images could be pulled from source."
        return None

    random_image = extract_image_from_string(choice(elements), IMAGE_START_VALUE, IMAGE_END_VALUE)

    return random_image


def extract_image_elements_from_url(url, xpath_format):
    retry_count = 0
    page = None

    while retry_count < 5 and page is None:
        try:
            page = requests.get(url)
        except requests.exceptions.ConnectionError:
            retry_count += 1
            print "Connection failed, retrying..."
            sleep(5)
            print "Retry Count: " + str(retry_count)
            continue

    if page is None:
        print "Request for image content failed. Aborting :("
        raise Exception('Failed to request image content.')

    tree = html.fromstring(page.content)

    return tree.xpath(xpath_format)


def extract_image_from_string(value, start_value, end_value):
    start_index = value.find(start_value) + len(start_value)
    end_index = value.find(end_value, start_index)

    return value[start_index:end_index]
