from lxml import etree,html
import requests

with open ('/home/axu/Projects/testbox/realtor/up04.html','r') as f:
     page = f.read()
#print page
tree = html.fromstring(page)
address = tree.xpath('//span[@class="list_lst_address"]/text()')
price = tree.xpath('//div[@class="m_property_lst_cnt_property_price"]/text()')

link = tree.xpath('//div[@class="m_property_lst_hdr_lft"]/a/text()')
num = tree.xpath('//div[@class="m_property_lst_cnt_property_listing_id"]/text()')

abed  = tree.xpath('//span[contains(@id,"list_lst_bed")]/text()')
abath = tree.xpath('//span[contains(@id,"list_lst_bath")]/text()')
bed = []
for i in range(1,10):
    sbed = 'list_lst_bed'+str(i)
    print i,sbed 
    try:
      bed.append(tree.xpath('//span[@id="'+sbed+'"]/text()'))
    except :
      bed.append('none')

ptype = tree.xpath('//div[contains(@id,"list_lst_propertytype")]/text()')
btype = tree.xpath('//div[contains(@id,"list_lst_buildtype")]/text()')
landsize  = tree.xpath('//div[contains(@id,"list_lst_landsizetotal")]/text()')
area  = tree.xpath('//div[contains(@id,"list_lst_sizeinterior")]/text()')


sales = tree.xpath('//a[contains(@id,"property_lst_cnt_realtor_details_realtor_lnk")]/text()')

desc = tree.xpath('//div[@class="m_property_lst_cnt_realtor_property_description"]/a/span/text()')
num0 = num[0][-8:]
print num,num0
print address,price,sales,desc,ptype,btype,landsize,bed,len(bed),len(sales)
