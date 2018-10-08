from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r"D:\\gecodrive\\geckodriver.exe")

# заходим в вк
driver.get("https://vk.com/")
# Ищем и кликаем на кнопку логина
log_btn = driver.find_element_by_id('index_login_button')
log_btn.click()

# Убеждаемся, что не залогинились (можно иначе)
try:
    log_btn = driver.find_element_by_id('index_login_button')
    print("Мы  не залогинились!")
except NoSuchElementException:
    print("Мы залогинились!")

# Вводим логин и пытаемся залогиниться
input_em = driver.find_element_by_id('index_email')
input_em.send_keys('Test@yandex.ru')
log_btn.click()

# Убеждаемся, что не залогинились (можно иначе)
try:
    log_btn = driver.find_element_by_id('index_login_button')
    print("Мы  не залогинились!")
except NoSuchElementException:
    print("Мы залогинились!")

# вводим неверный пароль и пытаемся залогиниться
input_pass = driver.find_element_by_id('index_pass')
input_pass.send_keys('123456T')
log_btn.click()

# Убеждаемся что на другой странице
wait_for_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login_reg_button"))
    )
if driver.current_url == "https://vk.com/":
    print("Мы Не сменили страницу!")
else:
    print("Мы сменили страницу!")

# Проверяем, на странице ошибки ли мы
try:
    log_mes_btn = driver.find_element_by_id('login_message')
    print("Мы на странице ошибки!")
except NoSuchElementException:
    print("Мы залогинились?")

# ищем кнопку регистрации и нажимаем
log_btn = driver.find_element_by_id('login_reg_button')
log_btn.click()

# Убеждаемс, что мы вновь на первой странице
wait_for_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ij_submit"))
    )

if driver.current_url == "https://vk.com/":
    print("Мы на первой странице!")
elif driver.current_url == "https://vk.com/join":
    print("Мы не на первой странице, но на ее аналоге.")
else:
    print("Мы не на первой странице! :с")

