"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("tech w/ tim")
time.sleep(5)
driver.quit()
"""

import requests

def validate_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        # Check if proxy works with Google
        google_response = requests.get("https://www.google.com", proxies=proxies, timeout=5)
        if google_response.status_code == 200:
            print(f"Proxy {proxy} is valid for Google")
            return True
        # Check if proxy works with Bing
        bing_response = requests.get("https://www.bing.com", proxies=proxies, timeout=5)
        if bing_response.status_code == 200:
            print(f"Proxy {proxy} is valid for Bing")
            return True
    except Exception as e:
        print(f"Proxy {proxy} failed: {e}")
    
    return False

# Read the proxies from your saved file
with open('proxies.txt', 'r') as file:
    proxies = file.readlines()

# Check and save valid proxies to valid_proxies.txt
with open('valid_proxies.txt', 'w') as valid_file:
    for proxy in proxies:
        proxy = proxy.strip()  # Remove any extra spaces or newline characters
        if validate_proxy(proxy):
            valid_file.write(f"{proxy}\n")


