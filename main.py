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
# for i in range(1, 101):
#     try:
#         # Adjusted XPath to start from 1
#         get_ele = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[1]")
#         file.write(str(get_ele.text))
#         print(f"GOT ELEMENT: {get_ele.text}")  # Printing the text of the element
    
#     except Exception as e:
#         print(f"Could not find element for row {i}: {e}")
#     time.sleep(2)

# THIS IS TO KIND OF IMPROVE THE CODE
def send_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        # Check if proxy works with Google
        google_response = requests.get("https://www.google.com", proxies=proxies, timeout=5)
        time.sleep(2)
        if google_response.status_code == 200:
            print(f"Proxy {proxy} is valid for Google")
            time.sleep(2)
            return True
            
        # Check if proxy works with Bing
        bing_response = requests.get("https://www.bing.com", proxies=proxies, timeout=5)
        time.sleep(2)
        if bing_response.status_code == 200:
            print(f"Proxy {proxy} is valid for Bing")
            time.sleep(2)
            return True
            
    except Exception as e:
        print(f"Proxy {proxy} failed: {e}")
    
    return False
    
valid_proxies = 0
current_table_row = 1
while valid_proxies <= 500:
    try:
        time.sleep(2)
        proxy = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{str(current_table_row)}]/td[1]")
        proxy = proxy.text.strip()
        print(f"Testing out {proxy}")
        time.sleep(2)
        with open("valid_proxies.txt", "w") as valid_file:
            if valid_proxies(proxy):
                time.sleep(2)
                print(f"Writing proxy {proxy} - {valid_proxies}")
                valid_file.write(f"{proxy}\n")
                valid_proxies = valid_proxies + 1
                time.sleep(2)
        current_table_row = current_table_row + 1
    except Exception as e:
        print(f"Error with row: {current_table_row} : {e}")
        

time.sleep(5)
driver.quit()
