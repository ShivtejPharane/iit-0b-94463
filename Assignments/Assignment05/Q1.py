from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.sunbeaminfo.in/internship")
# print("Page Title:", driver.title)
info =[]
# driver.implicitly_wait(5)
# table_body = driver.find_element(By.TAG_NAME,"tbody")
table_rows = driver.find_elements(By.XPATH,'//div//table//tbody/tr')

for rows in table_rows:
    col = rows.find_elements(By.XPATH,'.//td')
    # print(len(col))
    if len(col) == 8:
       info={
         "batch" :col[1].text.strip(),
         "batch duration" :col[2].text.strip(),
         "Start Date" : col[3].text.strip(),
         "end date " :col[4].text.strip(),
         "time" :col[5].text.strip(),
         "fees" :col[6].text.strip(),
         "Download" :col[7].text.strip()
       }
       print(info)

driver.quit()