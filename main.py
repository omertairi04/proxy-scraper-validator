import time
import threading
from proxies_scrapers.free_proxy_list import scrape_free_proxy_list
from proxies_scrapers.proxyscrape import scrape_proxy_list
from file_utils import append_to_file  # Import here

if __name__ == "__main__":
    threads = []
    
    thread1 = threading.Thread(target=scrape_proxy_list)
    thread2 = threading.Thread(target=scrape_free_proxy_list)
    
    threads.append(thread1)
    threads.append(thread2)
    
    thread1.start()
    thread2.start()
    
    for thread in threads:
        thread.join()
        
    print("Scraping completed.")
