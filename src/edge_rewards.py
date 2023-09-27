from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from pytrends.request import TrendReq
import pyautogui

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)


def login(email, password):
    driver.maximize_window()
    driver.get("https://login.live.com/")
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i0118"]')))
    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(Keys.ENTER)


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

pyautogui.PAUSE = 1

sleep(3)
pyautogui.press("f12")
pyautogui.press("left")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "m")
pyautogui.press("f5")

for c in range(len(brazil_trends)):
    pyautogui.hotkey("ctrl", "k")
    pesquisa = brazil_trends[0][c]
    pyperclip.copy(pesquisa)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
driver.quit()
