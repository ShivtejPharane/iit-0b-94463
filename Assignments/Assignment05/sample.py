from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.sunbeaminfo.com/internships")
driver.implicitly_wait(10)

print("Page Title:", driver.title)

# 1️⃣ Find the table
table = driver.find_element(By.TAG_NAME, "table")

# 2️⃣ Find tbody inside table
tbody = table.find_element(By.TAG_NAME, "tbody")

# 3️⃣ Find all rows
rows = tbody.find_elements(By.TAG_NAME, "tr")

# 4️⃣ Loop through rows
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")

    # IMPORTANT: skip invalid rows
    if len(cols) < 7:
        continue

    sr_no = cols[0].text
    batch = cols[1].text
    duration = cols[2].text
    start_date = cols[3].text
    end_date = cols[4].text
    time = cols[5].text
    fees = cols[6].text

    print(sr_no, batch, duration, start_date, end_date, time, fees)

driver.quit()
