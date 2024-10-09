import threading
import time

file_lock = threading.Lock()

def append_to_file(proxy):
    with file_lock:
        with open("all-proxies.txt", "a") as file:
            file.write(proxy + "\n")
