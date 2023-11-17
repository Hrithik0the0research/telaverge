import requests 
from instagram import scrape_data
import re
from bs4 import BeautifulSoup 

def social_media_scrap(url):
    r = requests.get(url) 
    
    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser') 
    x=[]
    # find all the anchor tags with "href"  
    for link in soup.find_all('a'): 
        x.append(link.get('href'))
        #print(link.get('href'))
    #print(x)
    urls=[]
    for i in x:
        if i!=None:
            if "facebook" in i:
                urls.append(i)
            elif "instagram" in i:
                urls.append(i)
            elif "linkedin" in i: 
                urls.append(i)
            elif "youtube" in i:
                urls.append(i)
            elif "twitter" in i:
                urls.append(i)
    #print(urls)
    socia_media={"instagram":None,"facebook":None,"twitter":None,"youtube":None,"linkedin":None}
    for i in urls:
        if "instagram.com" in i:
            socia_media["instagram"]=i 
        elif "facebook.com" in i:
            socia_media["facebook"]=i 
        elif "twitter.com" in i:
            socia_media["twitter"]=i 
        elif "youtube.com" in i:
            socia_media["youtube"]=i
        elif "linkedin" in i:
            socia_media["linkedin"]=i 
        
    #print(socia_media["instagram"])
    return socia_media
def followers_count(s):##counting followers
    count=scrape_data(s)
    return count
    

def company_reviews():
    from selenium import webdriver 
    from selenium.webdriver.chrome.service import Service as ChromeService 
    from webdriver_manager.chrome import ChromeDriverManager 
    options = webdriver.ChromeOptions() 
    
    # run browser in headless mode 
    options.headless= True 
    
    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install()), options=options) 
    url = 'https://in.indeed.com/cmp/Ey/reviews' 
    
    
    driver.get(url) 
    
    elements = driver.page_source
    h2=elements.find('<span class="css-15r9gu1 eu4oa1w0">')
    #nav=elements.find("nav")
    #print(elements[h2:])
    
    ExStr = []
    tags = ["span"]
    for tag in tags:
        seq = "<"+tag+">(.*?)</"+tag+">" 
        matches = re.findall(seq,elements)
        ExStr.extend(matches)
    #print(f"The extracted string is: {ExStr}")
    reviews=[]
    for i in ExStr:
        if '<span><span class="css-15r9gu1 eu4oa1w0">' in i:##take the certain span tag with class name
            reviews.append(i)
    #print(reviews)
    rev=[]
    for i in reviews:
        rev.append(i[41:])##appending reviews text part only and ignore other tags and html related text

    return rev
 