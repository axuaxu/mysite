from lxml import etree,html
import requests

with open ('/home/axu/Projects/testbox/realtor/sj01.html','r') as f:
     page = f.read()
#print page
tree = html.fromstring(page)
address = tree.xpath('//*[@id="m_property_dtl_address"]/text()')
price = tree.xpath('//*[@id="m_property_dtl_info_hdr_price"]/text()')
price1 = tree.xpath('//div[@class="m_property_dtl_info_hdr_lft_price"]/text()')
price2 = tree.xpath('//*[@id="list_lst_price1"]/text()')
link = tree.xpath('//div[@class="m_property_lst_hdr_lft"]/a/text()')
num = tree.xpath('//div[@class="m_property_lst_cnt_property_listing_id"]/text()')
#addr = tree.xpath('//div/[@class="m_property_lst_hdr_rgt"]/span/text()')
addr1 = tree.xpath('//*[@id="list_lst_address1"]/text()')
link1 = tree.xpath('//div[@class="m_property_lst_hdr/lft"]/a/@href')
addr2 = addr1[0].replace(',','-')
addr3 = addr2.replace(' ','-')
num0 = num[0][-8:]
url = 'https://www.realtor.ca/Residential/Single-Family/'+num0+'/'+addr3
al = tree.xpath('//a/@href')
alk = tree.xpath('//a[@class="property_lst_cnt_property_lnktop"]/@href')
print address,price,price1,price2,link,num,addr1,link1,addr3,num0,alk[0]

rl = alk[0].replace('https','http')
print rl
p = requests.get(rl)
tree2 = html.fromstring(p.content)
padd = tree2.xpath('//*[@id="m_property_dtl_address"]/text()')
ll = tree2.xpath('//*[@id="landsize_value"]/text()')
print padd,ll,p

#print url
