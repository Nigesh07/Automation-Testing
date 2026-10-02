import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # First Name
    driver.find_element(By.ID, "firstName").send_keys("nigesh")

    # Last Name
    driver.find_element(By.ID, "lastName").send_keys("sonaimuthu")

    # Email
    driver.find_element(By.ID, "userEmail").send_keys("nigesh@gmail.com")

    # Gender
    driver.find_element(By.ID, "gender-radio-1").click()

    # Mobile Number
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")

    # Hobbies
    driver.find_element(By.ID, "hobbies-checkbox-1").click()

    # Subject
    subject = driver.find_element(By.ID, "subjectsInput")
    subject.send_keys("Math")

    # Select Maths
    math_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'subjects-auto-complete__option') and normalize-space()='Maths']")
        )   
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        math_option
    )

    math_option.click()

    print("Maths selected successfully!")

    # Submit
    submit = driver.find_element(By.ID, "submit")

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit
    )

    wait.until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )

    submit.click()

    print("Submit clicked!")

    # Success message
    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "example-modal-sizes-title-lg")
        )
    )

    if message.text == "Thanks for submitting the form":
        print("Submit Successfully!")
    else:
        print("Submit Failed!")

except Exception as e:
    print("Error type:", type(e).__name__)
    print("The Error is:", e)

finally:
    driver.quit()