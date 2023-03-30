from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from time import sleep
import re

url = "https://subwaylistens.com/?subwaylistens&mkt=&priv=86&con=86&tou=86&lang=zh_TW"
email = "b10703027@gmail.com"
first_name = "FT"
last_name = "Tung"
store_num_1 = "25623"
# store_num_2 = '0'
date = "03/30/2023"
time_hour = "12"
time_minute = "59"

options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome("./chromedriver", chrome_options=options)
driver.get(url)

email_block = driver.find_element(By.ID, "spl_q_subway_customer_email_txt")
email_block.send_keys(email)
email_verify_block = driver.find_element(
    By.ID, "spl_q_subway_confirm_email_address_txt")
email_verify_block.send_keys(email)
first_name_block = driver.find_element(
    By.ID, "spl_q_subway_customer_first_name_txt")
first_name_block.send_keys(first_name)
last_name_block = driver.find_element(
    By.ID, "spl_q_subway_customer_last_name_txt")
last_name_block.send_keys(last_name)
begin_button = driver.find_element(By.ID, "buttonBegin")
begin_button.click()

store_num_block_1 = driver.find_element(By.ID, "storeNumberPart1")
store_num_block_1.send_keys(store_num_1)
# store_num_block_2 = driver.find_element(By.ID, "storeNumberPart2")
# store_num_block_2.send_keys(store_num_2)
date_block = driver.find_element(
    By.ID, "cal_q_subway_receipt_transaction_date_date_")
date_block.send_keys(date)
hour_button = driver.find_element(
    By.CLASS_NAME, "dropdown_dropdownTitle")
hour_button.click()

for i in range(1, 25):
    x_path = "//*[@id=\"content\"]/div[8]/fieldset/div/div/div[1]/div/div[2]/ul/li[" + \
        str(i) + "]"
    hour_block = driver.find_element(
        By.XPATH, x_path)
    if str(hour_block.text)[:2] == time_hour:
        hour_block.click()

minute_button = driver.find_element(
    By.XPATH, "//*[@id=\"content\"]/div[9]/fieldset/div/div/div[1]/div/div[1]")
minute_button.click()

for i in range(1, 61):
    x_path = "//*[@id=\"content\"]/div[9]/fieldset/div/div/div[1]/div/div[2]/ul/li[" + \
        str(i) + "]"
    minute_block = driver.find_element(
        By.XPATH, x_path)
    if str(minute_block.text)[:2] == time_minute:
        minute_block.click()

next_button = driver.find_element(By.ID, "buttonNext")
next_button.click()

button = driver.find_element(
    By.ID, "onf_q_subway_osat_satisfaction_web_scale_5_5")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_taste_quality_of_the_meal_web_scale_5_5")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_speed_of_service_web_scale_5_5")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_experience_with_staff_web_scale_5_5")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_cleanliness_of_restaurant_web_scale_5_5")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_likely_to_return_scale_11_10")
button.click()
button = driver.find_element(
    By.ID, "onf_q_subway_ltr_likely_scale_11_10")
button.click()

finish_button = driver.find_element(
    By.ID, "buttonFinish")
finish_button.click()

coupon = driver.find_element(
    By.XPATH, "//*[@id=\"content\"]/div[5]/div/span[1]")
print(coupon.text)

driver.close()
