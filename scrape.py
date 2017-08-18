from random import choice
from time import sleep

from lxml import html
from selenium import webdriver

from settings import IMAGE_URL, IMAGE_XPATH_FORMAT, IMAGE_START_VALUE, IMAGE_END_VALUE, GHOSTDRIVER_LOG_PATH


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
    driver = webdriver.PhantomJS(service_log_path=GHOSTDRIVER_LOG_PATH)

    while retry_count < 5 and page is None:
        try:
            # Scroll down a few times to ensure infinite scroll loads at least a few photos
            driver.get(url)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            page = driver.page_source
        except:
            retry_count += 1
            print "Connection failed, retrying..."
            print "Retry Count: " + str(retry_count)
            continue

    if page is None:
        print "Request for image content failed. Aborting :("
        raise Exception('Failed to request image content.')

    tree = html.fromstring(page)
    elements = tree.xpath(xpath_format)

    driver.quit()

    return elements


def extract_image_from_string(value, start_value, end_value):
    start_index = value.find(start_value) + len(start_value)
    end_index = value.find(end_value, start_index)

    return value[start_index:end_index]
