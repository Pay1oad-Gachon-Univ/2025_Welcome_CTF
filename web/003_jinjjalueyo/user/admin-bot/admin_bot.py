import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ADMIN_COOKIE_NAME = os.getenv("ADMIN_COOKIE_NAME", "ADMIN_TOKEN")
ADMIN_COOKIE_VALUE = os.getenv("ADMIN_COOKIE_VALUE", "SOME_SECRET")

FLAG_COOKIE_NAME = os.getenv("FLAG_COOKIE_NAME", "FLAG")
FLAG_COOKIE_VALUE = os.getenv("FLAG_COOKIE_VALUE", "CTF{...}")

ADMIN_BOT_TARGET = os.getenv("ADMIN_BOT_TARGET", "http://localhost:5000")

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")

    driver = webdriver.Chrome(options=chrome_options)
    print(f"Admin bot target: {ADMIN_BOT_TARGET}/admin/list")

    driver.get(f"{ADMIN_BOT_TARGET}/admin/list")
    driver.add_cookie({
        'name': ADMIN_COOKIE_NAME,
        'value': ADMIN_COOKIE_VALUE,
        'path': '/',
        'httpOnly': True
    })
    driver.add_cookie({
        'name': FLAG_COOKIE_NAME,
        'value': FLAG_COOKIE_VALUE,
        'path': '/'
    })

    while True:
        print(f"Admin bot target: {ADMIN_BOT_TARGET}/admin/list")
        driver.get(f"{ADMIN_BOT_TARGET}/admin/list")
        time.sleep(1)

        links = driver.find_elements(By.XPATH, "//a[contains(@href, '/admin/suggestion/')]")
        hrefs = []
        for link in links:
            link_href = link.get_attribute("href")
            hrefs.append(link_href)

        for href in hrefs:
            driver.get(href)
            print(f"Visited {href}")
            time.sleep(1)

        print("Admin bot cycle complete. Sleep 10s.")
        time.sleep(10)

if __name__ == "__main__":
    print("Start of main()")
    main()
