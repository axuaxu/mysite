from lxml import etree,html
import requests
import sqlite3

def savepage(content,c,conn):
    tree = html.fromstring(content)
    address = tree.xpath('//span[@class="list_lst_address"]/text()')
    price = tree.xpath('//div[@class="m_property_lst_cnt_property_price"]/text()')

    link = tree.xpath('//div[@class="m_property_lst_hdr_lft"]/a/text()')
    mlsnum = tree.xpath('//div[@class="m_property_lst_cnt_property_listing_id"]/text()')

    ptype = tree.xpath('//div[contains(@id,"list_lst_propertytype")]/text()')
    btype = tree.xpath('//div[contains(@id,"list_lst_buildtype")]/text()')
    land  = tree.xpath('//div[contains(@id,"list_lst_landsizetotal")]/text()')
    area  = tree.xpath('//div[contains(@id,"list_lst_sizeinterior")]/text()')

    desc = tree.xpath('//div[@class="m_property_lst_cnt_realtor_property_description"]/a/span/text()')
    #num0 = num[0][-8:]
    #print num,num0
    #print address,price,sales,desc,ptype,btype,landsize,bed,bath,len(bed),len(sales)
    storeys = ' '
    office = ' ' 

    bed = []
    bath = []
    sales = []
    for i in range(1,10):
        sbed = 'list_lst_bed'+str(i)
        sbath = 'list_lst_bath'+str(i)
        ssales = 'property_lst_cnt_realtor_details_realtor_lnk'+str(i)
        print i,sbed 
        try:
            bed.append(tree.xpath('//span[@id="'+sbed+'"]/text()'))
            bath.append(tree.xpath('//span[@id="'+sbath+'"]/text()'))
            sales.append(tree.xpath('//a[@id="'+ssales+'"]/text()'))
        except :
            bed.append(' ')
            bath.append(' ')
            sales.append(' ')
       
        o = i-1 
        iaddress = address[o]
        iprice = price[o]
        imlsnum = mlsnum[o][-8:]
        ibed = bed[o]
        ibath = bath[o]
        iptype = ptype[o]
        try:
             ibtype = btype[o]
        except IndexError:
             ibtype = " "
        iland = land[o]
        try:
             iarea = area[o]
        except IndexError:
             iarea = " "
        isales = sales[o]
        idesc = desc[o]

        sinsert1 = 'insert or ignore into mlist("address","price","mlsnum","bed","bath","ptype","btype","land","area","storeys","sales","office","desc") '
        sinsert2 = ' values (?,?,?,?,?,?,?,?,?,?,?,?,?) '
        #sinsert3 = '( iaddress,iprice,imlsnum,ibed,ibath,iptype,ibtype,iland,iarea,"",isales,"",idesc)'
        #sinsert4 = 'btype['+i+'],land['+i+'],area['+i+'],"",sales['+i+'],"",desc['+i+'])'      
       
        sinsert = sinsert1+sinsert2
        print sinsert
        print iaddress,iprice,imlsnum
        #c.execute(price,imlsnum,ibed,ibath,iptype,ibtype,iland,iarea,storeys,isales,office,idesc,))
        c.execute('insert or ignore into mlist(address,price,mlsnum,ptype,btype,land,area,desc) values (?,?,?,?,?,?,?,?)',(iaddress,iprice,imlsnum,iptype,ibtype,iland,iarea,idesc))
        conn.commit()
sqlfile = "realtor.sqlite"
conn = sqlite3.connect(sqlfile)
conn.text_factory = bytes
c = conn.cursor()
j = 1
for j in range(1,11):
    filename ='/home/axu/Projects/testbox/realtor/up'+str(j)+'.html' 
    print filename 
    with open (filename,'r') as f:
         page = f.read()

         savepage(page,c,conn)
         conn.commit()
         f.close()
   
conn.close()
