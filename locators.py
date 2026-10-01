import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
print("Brower opened Successfully!")

driver.maximize_window()
time.sleep(1)

page_title=driver.title
print(page_title)
time.sleep(1)

username=driver.find_element(By.ID,"username")
username.send_keys("student")
print("username checked Successsfully!")
time.sleep(1)

password=driver.find_element(By.ID,"password")
password.send_keys("Password123")
print("password checked Successfully!")
time.sleep(1)

submit=driver.find_element(By.ID,"submit")
submit.click()
print("submit checked Successfully!")
time.sleep(1)


