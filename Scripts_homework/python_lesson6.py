from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    input_y = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_y.send_keys(y)

    click_checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    click_checkbox.click()

    click_radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    click_radio.click()
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


