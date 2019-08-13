import os
import sys
import time
import random

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='/data/graphics/SpandanGraphsProject/geckodriver')


def scrape(d,start_page):
    print('scraping page %s',start_page)
    d.get('https://scholar.google.com/scholar?cites=1789338467385251622&start=%s'%start_page)
    el = driver.find_element_by_id('gs_bdy_ccl')
    text = el.text
    return text


for i in range(0,90,10):
    print('page number %s',%i)
    try:
        time.sleep(5 * random.random())
        scraped_page = scrape(driver,i)
#         print(scraped_page)
        with open('scraped_references.txt','a') as F:
            F.writelines(scraped_page)
    except:
        time.sleep(random.random()*4)
        print('stale webdriver, restarting')
        driver = webdriver.Firefox(options=options, executable_path='/data/graphics/SpandanGraphsProject/geckodriver')
        scraped_page = scrape(driver,i)
#         print(scraped_page)
        with open('scraped_references.txt','a') as F:
            F.writelines(scraped_page)
