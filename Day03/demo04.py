from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

print("Scan QR Code and wait...")
time.sleep(50)  
search_box = driver.find_element(
    By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"
)
search_box.send_keys("Tejas Babar Dkte")
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Message box
message_box = driver.find_element(
    By.XPATH, "//div[@contenteditable='true'][@data-tab='10']"
)
message_box.send_keys("hiii")
message_box.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()