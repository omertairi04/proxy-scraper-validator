from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class ProxyScrapper:    
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    def __init__(self, name, link):
        self.name = name
        self.link = link
        
    def scrape(self, link):
        pass
        


