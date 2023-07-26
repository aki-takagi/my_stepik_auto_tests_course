#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Lada")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("N")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("mail")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(3)

     # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
