from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://resortbaito-dive.com/works/search-result?area=2,4,3,5,6,7,8&prefecture=47,1&is_condition_search=true')

titles = driver.find_elements(By.XPATH, "//p[@class='job-title']/a[@class='title']")
print([x.text for x in titles])
