from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import requests
import sys

sys.stdout.reconfigure(line_buffering=True)

SELENIUM_URL = "http://selenium:4444/wd/hub"
TARGET_URL = "http://bookstack_app:80/login"
WEBSITE_ID = "91ae8bbc-1ab1-450a-94a1-2c1386cd8d9e"

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    return webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )

def wait_for_bookstack(url, retries=15, delay=5):
    print("Waiting for BookStack to be ready...")
    for i in range(retries):
        try:
            print(f"  Attempt {i+1}/{retries}...")
            r = requests.get(url, timeout=3)
            print(f"  Got status: {r.status_code}")
            if r.status_code == 200:
                print("BookStack is ready!")
                return
        except Exception as e:
            print(f"  Error: {e}")
        time.sleep(delay)
    raise Exception("BookStack never became ready")

def send_umami_pageview(url_path):
    try:
        response = requests.post(
            "http://umami:3000/api/send",
            json={
                "payload": {
                    "website": WEBSITE_ID,
                    "url": url_path,
                    "hostname": "bookstack_app",
                    "language": "en-US",
                    "screen": "1920x1080",
                    "title": "BookStack"
                },
                "type": "event"
            },
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            timeout=5
        )
        print(f"✓ Pageview sent for {url_path} - Status: {response.status_code}")
        if response.status_code != 200:
            print(f"  Response: {response.text}")
    except Exception as e:
        print(f"✗ Pageview send failed: {e}")

def simulate_user():
    driver = create_driver()

    try:
        print("Opening login page...")
        driver.get(TARGET_URL)
        time.sleep(5)
        send_umami_pageview("/login")

        print("Attempting login...")
        driver.find_element(By.NAME, "email").send_keys("admin@admin.com")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(8)
        send_umami_pageview("/dashboard")

        print("Login successful, navigating...")
        links = driver.find_elements(By.TAG_NAME, "a")
        clickable = [l for l in links if l.is_displayed() and l.get_attribute("href")]
        if clickable:
            chosen = random.choice(clickable)
            href = chosen.get_attribute("href")
            chosen.click()
            print(f"Clicked link: {href}")
            time.sleep(8)
            # Extract just the path from the full URL
            path = href.replace("http://bookstack_app", "").replace("http://localhost:8080", "")
            send_umami_pageview(path if path else "/")

    except Exception as e:
        print("ERROR:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    wait_for_bookstack(TARGET_URL)

    for i in range(10):
        print(f"Simulating user {i+1}")
        simulate_user()
        time.sleep(random.uniform(2, 5))