from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    if message.text == "You logged into a secure area!":
        print("Login successful!")
    else:
          print("Login Not successful!")

except Exception as e:
    print(f"Error: {e}")

finally:
     driver.quit()
