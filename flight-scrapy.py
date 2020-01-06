#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re
import requests as Request
import scrapy
import requests

class GoogleFlightsSpider(scrapy.Spider):
    name = 'products'
    
    currency = 'EUR'
    origin = 'CDG'
    destination = 'OLB'
    dateDeparture = '2020-05-09'
    dateReturn = '2020-05-09'

    # url='https://www.google.fr/flights#flt=CDG.OLB.2020-05-09*OLB.CDG.2020-05-16;c:EUR;e:1;s:0*0;sd:1;t:f'
    url = 'https://www.google.fr/flights#flt={}.{}.{}*{}.{}.{};c:{};e:1;s:0*0;sd:1;t:f'.format(origin, destination, dateDeparture, destination, origin, dateReturn, currency)


    def start_requests(self):
        yield scrapy.Request(
            self.url,
            dont_filter = True,
            callback=self.flight_page
        )

    def flight_page(self, response):
        yield scrapy.Request(
            self.url,
            dont_filter = True,
            callback=self.parse_flights
        )

    def parse_flights(self, response):
        print("def parse_flight")
        print(response.text)

        SET_SELECTOR = '.gws-flights-results__select-header'
        for quote in response.css(SET_SELECTOR):
            flight_price = './/div[@class="gws-flights-results__cheapest-price"]/text()'
            print(" Price: "+flight_price)

