# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:59:22 2019

@author: BITTU
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
    
    
#raw_html = simple_get('https://www.moneycontrol.com/stocksmarketsindia/?utm_source=Google&utm_medium=Search&utm_campaign=Traffic_SEM__Sok&utm_content=MC_Homepage&utm_source=Google&utm_medium=Paid&utm_campaign=sok_moneycontrol_search_nbr_markets_desktop&gclid=CjwKCAjwusrtBRBmEiwAGBPgE5caxis6b-LN0xDdI-P5XDocwcuErN7l9x5gorAR3MWfO_5wEoIoZxoCtDkQAvD_BwE')


no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')

print(no_html)


raw_html = simple_get('https://www.tensorflow.org/guide/keras/overview/')
#print(len(raw_html))
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
    print(i, li.text)
