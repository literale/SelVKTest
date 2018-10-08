from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r"D:\\gecodrive\\geckodriver.exe")
driver.get("https://vk.com/")

log_btn = driver.find_element_by_id('index_login_button')

log_btn.click()

input_em = driver.find_element_by_id('index_email')
input_em.send_keys('Test@yandex.ru')

log_btn.click()

input_pass = driver.find_element_by_id('index_pass')
input_pass.send_keys('123456T')

log_btn.click()

wait_for_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login_reg_button"))
    )

log_btn = driver.find_element_by_id('login_reg_button')
log_btn.click()