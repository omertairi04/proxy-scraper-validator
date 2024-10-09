from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from file_utils import append_to_file  # Import here

# Setup the Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

def scrape_free_proxy_list():
    try:
        driver.get('https://free-proxy-list.net/')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section[1]/div/div[2]/div/table"))
        )

        for i in range(1, 500):
            try:
                get_ele = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[1]")
                port_ele = driver.find_element(By.XPATH, f"/html/body/section[1]/div/div[2]/div/table/tbody/tr[{i}]/td[2]")

                proxy = f"{get_ele.text}:{port_ele.text}"
                print(f"Checking proxy: {proxy}")

                append_to_file(f"https://{proxy}")
                time.sleep(0.5)
            except Exception as e:
                print(f"Could not find element for row {i}: {e}")
                continue

        return True
    except Exception as e:
        print(f"EXCEPTION: {e}")
        return False
    finally:
        driver.quit()
