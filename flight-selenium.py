#!/usr/bin/python3

import sys
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

currency = 'EUR'
origin = 'CDG'
destination = 'OLB'
dateDeparture = '2020-05-09'
dateReturn = '2020-05-16'

# url='https://www.google.fr/flights#flt=CDG.OLB.2020-05-09*OLB.CDG.2020-05-16;c:EUR;e:1;s:0*0;sd:1;t:f'
url = 'https://www.google.fr/flights#flt={}.{}.{}*{}.{}.{};c:{};e:1;s:0*0;sd:1;t:f'.format(origin, destination, dateDeparture, destination, origin, dateReturn, currency)


logging.basicConfig(filename='parsing.log',level=logging.DEBUG)


def init_browser_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("window-size=1400,600")

    try:
        logging.debug("Webbrowser Opening Chrome")
        driver = webdriver.Chrome('chromedriver', options=chrome_options)
        logging.debug("Webbrowser: Opened Chrome")
    except:
        logging.error("Webbrowser: Error on opening Chrome")
        driver.close()
        sys.exit(1)
    return driver

def main():
    # All prices
    # FLIGHTS_SELECTOR = './/div[@class="flt-subhead1 gws-flights-results__price"]'
    # Cheapest price
    FLIGHTS_SELECTOR = './/div[@class="flt-subhead1 gws-flights-results__price gws-flights-results__cheapest-price"]'

    driver = init_browser_chrome()
    logging.debug("Webbrowser: Opened url")
    driver.get(url)

    delay = 2 # seconds
    logging.debug("Webbrowser: Waiting for page ready")
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gws-flights__flex-grow')))
        # driver.save_screenshot("gws-flights__flex-grow.png")
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gws-flights-results__result-list')))
        logging.debug("Webbrowser: Page is ready!")
    except TimeoutException:
        logging.debug("Webbrowser: Loading took too much time!")

    logging.debug("Scraper: Starting scraping")
    prices = driver.find_elements_by_xpath(FLIGHTS_SELECTOR)
    logging.info("Scraper: {} result(s) found".format(len(prices)))
    for price in prices:
        if price.text != '':
            print(price.text.split(' ')[0])
            logging.info("Scraper: Price={}".format(price))
    logging.debug("Scraper: Ended scraping")

    logging.debug("Webbrowser: Closing Chrome")
    driver.close()
    logging.debug("Webbrowser: Closed Chrome")

if __name__ == '__main__':
    main()
