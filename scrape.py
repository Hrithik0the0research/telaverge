from srcaping import social_media_scrap
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time 
import pandas as pd 
#London Victoria & Albert Museum URL

driver = webdriver.Chrome()
url = 'https://www.google.com/maps/place/Victoria+and+Albert+Museum/@51.4966392,-0.17218,15z/data=!4m5!3m4!1s0x0:0x9eb7094dfdcd651f!8m2!3d51.4966392!4d-0.17218'
driver.get(url)
#webdriver.Chrome.cm().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
#driver.find_element("xpath",'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button').click()
#to make sure content is fully loaded we can use time.sleep() after navigating to each page
#import time
#time.sleep(30)
try:
    driver.find_element(By.CLASS_NAME, "widget-pane-link").click()
except Exception:
    response = BeautifulSoup(driver.page_source, 'html.parser')
    # Check if there are any paid ads and avoid them
    if response.find_all('span', {'class': 'ARktye-badge'}):
        ad_count = len(response.find_all('span', {'class': 'ARktye-badge'}))
        li = driver.find_elements(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
        li[ad_count].click()
    else:
        driver.find_element(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd").click()
        time.sleep(5)
    driver.find_element(By.CLASS_NAME, "widget-pane-link").click()
#Find the total number of reviews
total_number_of_reviews = driver.find_element('xpath','//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]').text.split(" ")[0]
total_number_of_reviews = int(total_number_of_reviews.replace(',','')) if ',' in total_number_of_reviews else int(total_number_of_reviews)
#Find scroll layout
scrollable_div = driver.find_element('xpath','//*[@id="pane"]/div/div[1]/div/div/div[2]')
#Scroll as many times as necessary to load all reviews
for i in range(0,(round(total_number_of_reviews/10 - 1))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                scrollable_div)
        time.sleep(1)
response = BeautifulSoup(driver.page_source, 'html.parser')
reviews = response.find_all('div', class_='ODSEW-ShBeI NIyLF-haAclf gm2-body-2')
def get_review_summary(result_set):
    rev_dict = {'Review Rate': [],
        'Review Time': [],
        'Review Text' : []}
    for result in result_set:
        review_rate = result.find('span', class_='ODSEW-ShBeI-H1e3jb')["aria-label"]
        review_time = result.find('span',class_='ODSEW-ShBeI-RgZmSc-date').text
        review_text = result.find('span',class_='ODSEW-ShBeI-text').text
        rev_dict['Review Rate'].append(review_rate)
        rev_dict['Review Time'].append(review_time)
        rev_dict['Review Text'].append(review_text)
    import pandas as pd    
    return(pd.DataFrame(rev_dict))
rev=get_review_summary(reviews)
print(rev)
"""
#from bs4 import BeautifulSoup
#import requests
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Referer':'https://in.indeed.com/cmp/Ey/reviews','Cookie':'CTK=1h2ado2ougpei800; cf_clearance=rPbaSsG2qslu6Oqx0mFVFXbtl_uG3HBvNrjkl69RH7c-1691865522-0-1-ee79d636.d45a2344.f56d2a4e-0.2.1691865522; indeed_rcc=CTK; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtfR4BymUxew6eygcWBiPdP4="; _ga=GA1.2.251940113.1695749577; _gcl_au=1.1.281252904.1695749577; LC="co=IN"; SOCK="sopZU8dFmlXDIXZ9CNwkz7IQ_iQ="; SHOE="1h0wu0lPGc7UyoxOrDXvuY-oWclI914XQD4mwn94cqGQJVlvSsTzV-Tz25AD5RNCjHQVOJhXGcyInAhkMSCnKrSBhOGrGysqPkIGIGsT52HGYUx-R5OpmM78u1klfG-4ztOPUTw9CmeWERaQSWg_wvMT1g=="; _gid=GA1.2.191486547.1699714130; CMP_VISITED=1; cmppmeta="eNoBSAC3/x9MWZbIfDJl9Dc06nwfemJiseUKs7Z6u7e2FAym4ZL30w4+Z6MzWrsuWNIXerG3UbnXIEWTMNieY6Yn81Lq++x7ricxxL4nRATwJCg="; CO=IN; IRF=7YXfKDzcx1JT-QT4QnjgSBxoeWd-bJfGJVEnksMzWzzhLYVke-XK0A==; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Nov+11+2023+20%3A28%3A24+GMT%2B0530+(India+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=7b4ff167-39ae-469a-8e56-e5dc12b224c0&interactionCount=1&landingPath=https%3A%2F%2Femployers.indeed.com%2Fp%2Fposting%3Fco%3DIN%26hl%3Den_IN%26from%3Dgnav-menu-acme--acme-webapp%26ikw%3Dgnav-header-hire%26isid%3Demployerlink-IN%26trafficTK%3D1h2ado2ougpei800%26jstm%3D1699714589482%26_ga%3D2.138927475.191486547.1699714130-251940113.1695749577&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0; CO=IN; LV="LA=1699770678:CV=1699770678:TS=1699770678"; hpnode=1; indeed_rcc="cmppmeta:CTK"; INDEED_CSRF_TOKEN=yiTSZZJsoQfZ4FB6eRxNEM39Pn23s6Si; bvcmpgn=direct; _cfuvid=GBbsv7xt7YleyCojU2R3iCwhTJtEzE2fEH_0PwTICX8-1699799309965-0-604800000; PPID=eyJraWQiOiIzN2FjZGI4MC04M2NkLTQ3YjItODAxOS1mMzE3ZjhiNjRiNmIiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI2YmE0ZTllOTMyYzEyYWRmIiwibGFzdF9hdXRoX3RpbWUiOjE2OTY5NjM4OTczODUsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdXRoIjoiZ29vZ2xlIiwiY3JlYXRlZCI6MTYwMDg0ODk0NzAwMCwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwibGFzdF9hdXRoX2xldmVsIjoiU1RST05HIiwibG9nX3RzIjoxNjk2OTYzODk3Mzg1LCJhdWQiOiJjMWFiOGYwNGYiLCJyZW1fbWUiOnRydWUsImV4cCI6MTY5OTgwMTExMSwiaWF0IjoxNjk5Nzk5MzExLCJlbWFpbCI6ImhyaXRoaWtwYXVsMjAwMUBnbWFpbC5jb20ifQ.jvhK18XSy0EuCAxkTqbVCFOmpgge8-tPZD9K-nbMam7nTUI2SyHjLXQq13Abd_D7cbHfr2T_IK5j2mi-isCMaw; CSRF=hG6Gr9GqN6Fp5u7eWIAp4f57FRuteTGw; ENC_CSRF=kIDiJnOPFi4ka9WpEuT20yS5iau463mB; JSESSIONID=B20F17BE408CC0231D30A7C60BBE5CBA; __cf_bm=.2P7iFyI99_DosDtzBwRQPSTjR78jNjbjVziqiYis4M-1699801113-0-AUEi5ODqZl/c+I0HzWQARLIgJHXam1YKdRzo20zbBbK1dpfqHitV6zv1c2Lg9cBYXgy+ajbFDbdPxiUEZBLbX/k='}
#url=requests.get("https://in.indeed.com/cmp/Ey/reviews",headers=headers)
##print(url.status_code)
#bs=BeautifulSoup(url.content,"html.parser")
#s=bs.find_all("h2",{"class":"css-1edqxdo e1tiznh50"})
#print(s)
#import requests
#session = requests.Session()
#response = session.get('https://in.indeed.com/cmp/Ey/reviews')

#print(type(s[0]))
#cookies=session.cookies.get_dict()
#print(cookies)
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Referer':'https://in.indeed.com/cmp/Ey/reviews',cookies}
#url=requests.get("https://in.indeed.com/cmp/Ey/reviews",headers=headers)
#print(url.status_code)
#bs=BeautifulSoup(url.content,"html.parser")
##s=bs.find_all("h2",{"class":"css-1edqxdo e1tiznh50"})
#print(s)
'''
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless= True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
url = 'https://www.indeed.com/cmp/Tata-Consultancy-Services-(tcs)/reviews' 
 
 
driver.get(url) 
 
elements = driver.page_source
h2=elements.find('<span class="css-15r9gu1 eu4oa1w0">')
#nav=elements.find("nav")
#print(elements[h2:])
import re
ExStr = []
tags = ["span"]
for tag in tags:
   seq = "<"+tag+">(.*?)</"+tag+">"
   matches = re.findall(seq,elements)
   ExStr.extend(matches)
#print(f"The extracted string is: {ExStr}")
reviews=[]
for i in ExStr:
   if '<span><span class="css-15r9gu1 eu4oa1w0">' in i:
      reviews.append(i)
#print(reviews)
rev=[]
for i in reviews:
   rev.append(i[41:])

print(rev)
'''
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless= True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
x=social_media_scrap("https://www.tcs.com/")
print(x)
instagram=x['instagram']
print(instagram)
url = instagram
 
 
driver.get(url) 
 
elements = driver.page_source
print(elements)
"""
h2=elements.find('<span class="css-15r9gu1 eu4oa1w0">')
#nav=elements.find("nav")
#print(elements[h2:])
import re
ExStr = []
tags = ["span"]
for tag in tags:
   seq = "<"+tag+">(.*?)</"+tag+">"
   matches = re.findall(seq,elements)
   ExStr.extend(matches)
#print(f"The extracted string is: {ExStr}")
reviews=[]
for i in ExStr:
   if '<span><span class="css-15r9gu1 eu4oa1w0">' in i:
      reviews.append(i)
#print(reviews)
rev=[]
for i in reviews:
   rev.append(i[41:])

print(rev)
"""