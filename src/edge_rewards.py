from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from pytrends.request import TrendReq


driver = webdriver.Edge()


def login(email, password):
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://login.live.com/")
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(Keys.ENTER)


if __name__ == "__main__":
    login("email", "password")

    pytrend = TrendReq()
    brazil_trends = pytrend.trending_searches(pn="brazil")
    driver.get("https://www.bing.com/")
    sleep(3)
    try:
        element = driver.find_element(By.XPATH, '//*[@id="bnp_btn_accept"]/a')
        element.click()
    except Exception as e:
        print(e)

    for c in range(len(brazil_trends)):
        search = brazil_trends[0][c]
        pyperclip.copy(search)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(search)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(Keys.ENTER)
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').clear()

    world_trends = pytrend.trending_searches()
    for c in range(len(world_trends)):
        search = world_trends[0][c]
        pyperclip.copy(search)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(search)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').send_keys(Keys.ENTER)
        sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="sb_form_q"]').clear()

    driver.quit()
