from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    find_x = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = find_x.text
    find_y = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = find_y.text
    sum_xy = int(x) + int(y)
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(str(sum_xy))
    
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


