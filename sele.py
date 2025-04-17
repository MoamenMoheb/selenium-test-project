from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def wait_for_radio_buttons(driver, timeout=10):
    """Wait for radio buttons to be present and return them with their labels."""
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='radio']"))
    )
    
    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    radio_labels = []
    
    for radio in radio_buttons:
        radio_id = radio.get_attribute("id")
        if radio_id:
            label = driver.find_element(By.CSS_SELECTOR, f"label[for='{radio_id}']")
            radio_labels.append(label)
            print(f"Radio ID: {radio_id}, Label Text: {label.text.strip()}")
    
    return radio_labels

def select_random_option_and_continue(driver):
    """Select a random radio option and click next."""
    radio_labels = wait_for_radio_buttons(driver)
    
    if radio_labels:
        random_label = random.choice(radio_labels)
        driver.execute_script("arguments[0].click();", random_label)
        print(f"Selected option: {random_label.text.strip()}")
    else:
        print("No interactable radio buttons found.")
    
    # Click the Next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.next"))
    )
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(1)  # Small delay to allow page transition

while True:
    # Initialize driver
    driver = webdriver.Chrome()
    driver.get("https://www.everystepindiabetes.com/take-the-test/?fbclid=IwZXh0bgNhZW0CMTEAAR24Vss_qSb0aBwUWRBXs-Dkah1amyaooKlAfgpEUxktLP7g5BQHCokOjOI_aem_O1F6_Tvecf0k33D96Mhyhw#/question/1")

    # Process each question page
    for _ in range(8):  # Assuming there are 3 questions
        select_random_option_and_continue(driver)

    random_height = random.randint(140, 190)

    # Find the input field and send the random value
    height_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='height']"))
    )

    # Clear the field first (in case there's any default value)
    height_input.clear()

    # Send the random value
    height_input.send_keys(str(random_height))

    #random weight
    random_weight = random.randint(50, 100)
    #find the input field and send the random value
    weight_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='weight']"))
    )

    # Clear the field first (in case there's any default value)
    weight_input.clear()

    # Send the random value
    weight_input.send_keys(str(random_weight))
    # Click the Next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.next"))
    )
    driver.execute_script("arguments[0].click();", next_button)

    time.sleep(2)  # Wait 2 seconds before trying to close
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.wrapper > div.arrow"))
    )
    close_button.click()
    # Wait for user input before quitting
    time.sleep(2)
    driver.quit()