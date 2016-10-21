# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import codecs
from lxml import html
import sqlite3
import re
from random import randint


sqlite_file = "realtor.sqlite"
conn = sqlite3.connect(sqlite_file)
conn.text_factory = bytes
c = conn.cursor()
murl = "http://www.realtor.ca/Residential/Single-Family/17444420/58-MORRISON-Road-SAINT-JOHN-New-Brunswick-E2N1G9"
driver = webdriver.Firefox()
#driver.set_window_position(1200,0)
#driver.set_window_size(100,500)
driver.get(murl)
#elem = driver.find_element_by_class_name("m_hme_srch_ipt_plchldr")
#elem.send_keys("Saint John,NB")
#elem.send_keys(Keys.RETURN)
#address0 = driver.find_element_by_xpath('m_property_dtl_address')
pp = driver.find_element_by_id('m_property_dtl_info_hdr_price')
print pp
driver.close()
#conn.commit()
conn.close()
                                                          
