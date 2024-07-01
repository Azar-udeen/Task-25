from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the IMDb search page
    driver.get("https://www.imdb.com/search/name/")

    # Wait until the name input box is present and enter the name "Tom Hanks"
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    name_input.send_keys("Tom Hanks")

    # Wait until the gender select box is clickable and select "Male"
    gender_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gender"))
    )
    for option in gender_select.find_elements(By.TAG_NAME, 'option'):
        if option.text == "Male":
            option.click()
            break

    # Wait until the born date input boxes are present and enter the dates
    born_date_from = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birth_date_min"))
    )
    born_date_from.send_keys("1950-01-01")

    born_date_to = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "birth_date_max"))
    )
    born_date_to.send_keys("1960-01-01")

    # Wait until the search button is clickable and click it
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Search')]"))
    )
    search_button.click()

    # Wait until the search results are loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "lister-item"))
    )

    # Print the number of results found
    results = driver.find_elements(By.CLASS_NAME, "lister-item")
    print(f"Number of results found: {len(results)}")

finally:
    # Close the WebDriver
    driver.quit()