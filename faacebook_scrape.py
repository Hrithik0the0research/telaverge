from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup  
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
options = webdriver.ChromeOptions() 

# run browser in headless mode 
options.headless= True 

# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
    ChromeDriverManager().install()), options=options) 
login_url = 'https://www.facebook.com/?stype=lo&deoia=1&jlou=AffGSodggDgRGn1dX6l0-eLKgoSEg-3I8ziTHJA3RN5qkTSVIM8KD7L-WCs8Z6nKxUQekvgb-B-NOwL_Rp-ntR7BZjJAJvbnBxBljAXqR9ZUIg&smuh=15599&lh=Ac-CSWkD-ajEGGu04nA' 
driver.get(login_url)
USERNAME = "hrithikpaul2001@gmail.com"
PASSWORD ="hrithik@123"
elementID = driver.find_element(By.ID,'email')
elementID.send_keys(USERNAME)
elementID = driver.find_element(By.ID,'pass')
elementID.send_keys(PASSWORD)
elementID.submit()
profile_url = "https://www.facebook.com/TataConsultancyServices"

driver.get(profile_url) 
title = (
    WebDriverWait(driver=driver, timeout=10)
    .until(visibility_of_element_located((By.CSS_SELECTOR, "a")))
    .text
)
ps=BeautifulSoup(driver.page_source,"html5lib")
print(ps)