import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.maximize_window()

time.sleep(5)

wait=WebDriverWait(driver,10)


username=WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH,"//*[@id='username']"))
)

username.send_keys("student")

password=wait.until(
    EC.visibility_of_element_located((By.XPATH,"//*[@id='password']"))
)

password.send_keys("Password123")

old_url=driver.current_url

login_button=wait.until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='submit']"))
)

login_button.click()

# wait.until(
#     EC.url_changes(old_url)
# )

# wait .until(
#     EC.url_contains("logged-in-successfully")
# )

# wait.until(
#     EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/")
# )

print("Submit Successfully")

driver.quit()

wait.until(
    EC.presence_of_element_located((By.ID,"submit"))
)


