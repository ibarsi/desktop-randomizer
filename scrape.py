import json
from random import sample

from lxml import html
import requests


def get_random_image():
    with open('config.json') as config_file:
        config = json.load(config_file)

    elements = extract_image_elements_from_url(config['image_url'], config['image_xpath_format'])

    random_image = extract_image_from_string(sample(elements, 1)[0], config['image_start_value'], config['image_end_value'])

    return random_image


def extract_image_elements_from_url(url, xpath_format):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    return tree.xpath(xpath_format)


def extract_image_from_string(value, start_value, end_value):
    start_index = value.find(start_value) + len(start_value) + 1
    end_index = value.find(end_value, start_index)

    return value[start_index:end_index]
