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

murl = "https://www.realtor.ca"
driver = webdriver.Firefox()
#driver.set_window_position(1200,0)
#driver.set_window_size(100,500)
driver.get(murl)
elem = driver.find_element_by_class_name("m_hme_srch_ipt_plchldr")
elem.send_keys("Saint John,NB")
elem.send_keys(Keys.RETURN)
sp = randint(23,26)
time.sleep(sp)

parser = html.fromstring(driver.page_source,driver.current_url)
today = datetime.now()
udate = ''

for i in range(1,3):

    for j in range(1,9):
        # [@id='list_lst_address2']
        rlink = driver.find_element_by_class_name("property_lst_cnt_property_lnktop")
        rlink.click()
        

        second_driver = webdriver.Firefox()
        second_driver.set_window_position(1000,0)
        second_driver.set_window_size(100,600)
        surl =  driver.current_url
        second_driver.get(surl)

        second_parser = html.fromstring(second_driver.page_source,second_driver.current_url)
        # setFields(udate,surl,area,second_parser,c,conn)
        xaddress = second_parser.xpath('//*[@id="m_property_dtl_address"]/text()') 
        print xaddress    
   
        second_driver.close()
    sp = randint(1,5)
    time.sleep(sp)
    #[@id='listView']/div[1]/div[2]/div/button[2]
    driver.find_element_by_xpath(".//[@id='listView']/div[1]/div[2]/div/button[2]").click()
    sp = randint(3,6)
    time.sleep(sp)
    parser = html.fromstring(driver.page_source,driver.current_url)
driver.close()
#conn.commit()
conn.close()
                                                          
