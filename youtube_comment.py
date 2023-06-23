from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()

options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)


url = 'https://www.youtube.com/watch?v=OZ9MpW_G6Co'

driver.implicitly_wait(10) # 페이지 로딩까지 10초 기다림
driver.get(url)

time.sleep(10) # DOM이 다 그려질 때까지 script 실행 지연

prev_height = driver.execute_script('return document.querySelector("#content").scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.querySelector("#content").scrollHeight);')
    time.sleep(5)
    
    curr_height = driver.execute_script('return document.querySelector("#content").scrollHeight')
    if curr_height == prev_height:
        break
    prev_height = curr_height

comment_list = driver.find_elements(By.TAG_NAME, 'ytd-comment-thread-renderer')

a = []

for comment in comment_list:
    username = comment.find_element(By.CSS_SELECTOR, '#author-text > span').text
    content = comment.find_element(By.CSS_SELECTOR, '#content-text').text
    a.append({'username': username, 'content': content})


print(a)

