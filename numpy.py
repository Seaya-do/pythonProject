import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

webdriver_service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=webdriver_service, options=option)


url = "https://www.gimpo.go.kr/masan/index.do"
driver.get(url)

time.sleep(3)
print(driver.page_source)
