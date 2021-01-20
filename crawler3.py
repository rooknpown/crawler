from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs


def getdata(startpage=1,count=100,outfilename="output.txt"):
    
    
    driver=webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)
    #driver.maximize_window()
    # 시작페이지 
    url='https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgList.jsp?menuSeq=679'
    driver.get(url)
   
    # page 이동
    driver.execute_script("document.getElementById('bbs_page').value = "+str(startpage)+";")  
    driver.find_element_by_css_selector("a.go_btn").click()
    time.sleep(0.5)
    
    element = driver.find_element_by_id('search_val_v')
    element.send_keys("대전")
    driver.find_elements_by_class_name('search_btn')[0].click()
    
    time.sleep(3.0)
    
    

    out=open(outfilename,"w",encoding="utf-8")
    errorcount=0
    for i in range(count):
        try:
            driver.find_elements_by_id('bbs_tr_0_bbs_title')[i].click()
            time.sleep(1.0)
            replys=driver.find_element_by_css_selector('div.boardView')
            tlist=replys.find_elements_by_id('sj')
            title=tlist[0].text
            text=replys.find_elements_by_id('cn')[0].text
            text=text.replace("\n",",")
            print(i,errorcount,title,text)
            if(len(title)==0):
                break
            out.write(title)
            out.write(text)
            out.write("\n")
            replys=driver.find_element_by_css_selector('ul.boardView_listWrap')
            
            # 다음 목록 
            replys.find_elements_by_class_name('list_btn')[0].click()
            time.sleep(1.0)
        except:
            errorcount+=1

    out.close() 
    driver.close()


####### 사용법 예시 
getdata(startpage=1,count=10,outfilename='out0.txt')
# getdata(startpage=900,count=10,outfilename='out900.txt')

