from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()

# options.add_experimental_option('detect', True)

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)


url = 'https://movie.daum.net/ranking/reservation'

driver.implicitly_wait(5) # 페이지 로딩까지 5초 기다림
driver.get(url)

order_list = driver.find_element(By.CSS_SELECTOR, 'ol.list_movieranking')

def extract_text(el, selector):
    return list(map(lambda element: element.text, el.find_elements(By.CSS_SELECTOR, selector)))

title = extract_text(order_list, 'strong.tit_item > a.link_txt')
grade = extract_text(order_list, 'span.txt_append span.txt_grade')
rate = extract_text(order_list, 'span.txt_append span.txt_num')
release = extract_text(order_list, 'span.txt_info span.txt_num')

df = {'제목': title, '평점': grade, '예매율': rate, '개봉': release}

df = pd.DataFrame(df)