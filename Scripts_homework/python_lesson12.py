from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
    )

    click_btn = browser.find_element(By.CSS_SELECTOR, '#book')
    click_btn.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input_y = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_y.send_keys(y)

    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


