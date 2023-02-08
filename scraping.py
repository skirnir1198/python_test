from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://resortbaito-dive.com/works/search-result?area=2,4,3,5,6,7,8&prefecture=47,1&is_condition_search=true')
num = driver.find_element(By.CLASS_NAME, "num-info") #求人数取得
jobs = 0 #現在表示中の求人数
works = []
i=0 #while文回数

while int(num.text) > jobs:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #最下部までスクロール
    time.sleep(2)
    jobs = len(driver.find_elements(By.TAG_NAME, "app-job-item"))
    print(jobs)

# 回数指定
# while i < 1:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #最下部までスクロール
#     time.sleep(2)
#     jobs = len(driver.find_elements(By.TAG_NAME, "app-job-item"))
#     i += 1

info = driver.find_elements(By.XPATH, "//ul[@class='job-recruitment-icon']")
all_info = [x for x in info]
for item in all_info:
    place = item.find_elements(By.CLASS_NAME, "recruitment-text")
    works.append({
        'place':place[0].text,
        'type':place[1].text,
        'wage':place[2].text,
        'period':place[3].text
        })

print(works[1]['place'])