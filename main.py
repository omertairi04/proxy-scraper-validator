from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://free-proxy-list.net/')

# Wait for the table to be present in the DOM
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/div/div[2]/div/table"))
)

# Select the table element
table = driver.find_element(By.XPATH, "/html/body/section[1]/div/div[2]/div/table")



def write_to_file(fileName):
    file = open(str(fileName), "a")
    try:
        file.write("Writing to file")
    except Exception as e:
        print(f"Could not write \nEXCEPTION: {e}")

file = open("all-proxies.txt", "a")

# Use 1-based indexing for rows
# THIS SAVES ELEMENTS TO all-proxies.txt
for i in range(1, 330):
    try:
        # Adjusted XPath to start from 1
        get_ele = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[1]")  # IP address
        port_ele = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[2]")  # Port
        https_support = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[7]")  # HTTPS column

        proxy = f"{get_ele.text}:{port_ele.text}"
        print(f"Checking proxy: {proxy}")

        # Only save proxies that support HTTPS
        if https_support.text == "yes":
            file.write(f"https://{proxy}\n")
            print(f"Saved HTTPS proxy: {proxy}")
        else:
            print(f"Skipping non-HTTPS proxy: {proxy}")

        time.sleep(1)
    except Exception as e:
        print(f"Could not find element for row {i}: {e}")
        break
    time.sleep(2)
    
file.close()

time.sleep(5)
driver.quit()
