import requests
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False
    
def main():
    url = "https://google.com"
    if check_website(url):
        print(f"{datetime.now()}: {url} is up.")
    else:
        print(f"{datetime.now()}: {url} is down.")

if __name__ == "__main__":
    main()
    