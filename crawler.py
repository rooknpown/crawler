import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from urllib.request import URLError


# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f1 = open(os.path.join(BASE_DIR, 'weblink.txt'), 'r')
f2 = open(os.path.join(BASE_DIR, 'linkname.txt'), 'r')
# f3 = open(os.path.join(BASE_DIR, 'tablename.txt'), 'r')
# f4 = open(os.path.join(BASE_DIR, 'tabletype.txt'), 'r')

lines = f1.readlines()
locs = f2.readlines()
# tnames = f3.readlines()
# ttypes = f4.readlines()
leng = len(lines)
for i in range(leng):
    # page = requests.get(line[:-1])
    # attrs = {ttypes[i][:-1] : tnames[i][:-1]}
    try:
        table = pd.read_html(lines[i][:-1],match = '노출일시')[0]
        table.to_csv(os.path.join(BASE_DIR, 'data\\'+ str(datetime.today())[:10] + locs[i][:-1] +'.csv'))
        print(table)
        print(str(datetime.today())[:10])
    except URLError as e:  
        continue
    # doc = lh.fromstring(page.content)
    # tr_elements = doc.xpath('//tr')

    # #Create empty list
    # col=[]
    # i=0
    # #For each row, store each first element (header) and an empty list
    # for t in tr_elements[0]:
    #     i+=1
    #     name=t.text_content()
    #     print ('%d:"%s"'%(i,name))
    #     col.append((name,[]))


   

    # with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    #     json.dump(data, json_file)

f1.close()
f2.close()