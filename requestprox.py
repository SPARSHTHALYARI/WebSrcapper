import requests


def fetch_data_with_proxy(url, proxy):
    proxies = {
        "http": proxy,
        "https": proxy
    }

    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return None


def main():
    url = "https://medium.com/pitfall/bye-bye-spotify-37bb823839d2"  # Replace with the URL you want to scrape
    proxy = "103.62.237.102:8080"  # Replace with a proxy IP and port

    data = fetch_data_with_proxy(url, proxy)
    if data:
        # Process and work with the fetched data
        print(data)


if __name__ == "__main__":
    main()
