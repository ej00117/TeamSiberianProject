from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

base_url = "http://localhost:8080"

driver.get(base_url + "/login")

email_box = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
password_box = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

email_box.clear()
email_box.send_keys("admin@admin.com")
time.sleep(1)

password_box.clear()
password_box.send_keys("password")
time.sleep(1)

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
driver.execute_script("arguments[0].click();", login_button)
time.sleep(5)

for i in range(5):
    print(f"Round {i+1}")

    links = driver.find_elements(By.TAG_NAME, "a")
    clickable_links = []

    for link in links:
        try:
            href = link.get_attribute("href")
            if link.is_displayed() and link.is_enabled() and href:
                clickable_links.append(link)
        except:
            continue

    if clickable_links:
        try:
            chosen_link = random.choice(clickable_links)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", chosen_link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", chosen_link)
            print("Clicked a link")
            time.sleep(3)
        except Exception as e:
            print("Click skipped:", e)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    for box in inputs:
        try:
            input_type = box.get_attribute("type")
            if box.is_displayed() and box.is_enabled() and input_type in ["text", "search"]:
                box.clear()
                box.send_keys("test")
                box.send_keys(Keys.ENTER)
                print("Typed into a box")
                time.sleep(3)
                break
        except:
            continue

input("Press Enter to close...")
driver.quit()