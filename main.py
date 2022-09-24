from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#chromedriver.exe 불러오기
driver = webdriver.Chrome('/Users/s9912/chromedriver')
#naver 불러오기
driver.get('https://www.naver.com')
driver.implicitly_wait(3)

# 검생창 불러오기
e = driver.find_element(By.ID, 'query')
# 검생창에 abc 입력
e.send_keys('abc')
# 검생창에 ENTER 키 입력
e.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()