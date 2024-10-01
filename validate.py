import requests

# Function to test if a proxy works
def test_proxy(proxy):
    # URLs to test against
    target_urls = ["https://www.google.com", "https://www.bing.com"]
    proxies = {
        "http": proxy,
        "https": proxy
    }
    
    for url in target_urls:
        try:
            # Send a GET request using the proxy
            response = requests.get(url, proxies=proxies, timeout=5)
            if response.status_code == 200:
                print(f"Proxy {proxy} works on {url.split('//')[1]}")
                return True
        except requests.exceptions.RequestException as e:
            print(f"Proxy {proxy} failed on {url.split('//')[1]}: {e}")
    
    return False

# Read proxies from all-proxies.txt and validate them
with open("all-proxies.txt", "r") as file:
    proxies = file.readlines()

# Prepare to write valid proxies
with open("validate-proxies.txt", "a") as valid_file:
    for proxy in proxies:
        proxy = proxy.strip()  # Remove any extra whitespace or newlines
        print(f"Testing proxy: {proxy}")
        
        if test_proxy(proxy):
            valid_file.write(proxy + "\n")  # Save valid proxy
            print(f"Saved valid proxy: {proxy}")

print("Validation complete!")
