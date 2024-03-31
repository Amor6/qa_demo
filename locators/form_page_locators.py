import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    GENDER = (By.XPATH, f'//label[@for="gender-radio-{random.randint(1,3)}"]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    DATE_OF_BIRTH = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, "#subjectsInput")
    HOBBIES = (By.XPATH, f'//label[@for="hobbies-checkbox-{random.randint(1,3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.XPATH, '//div[@id="state"]')
    INPUT_STATE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    STATE_TEXT = (By.XPATH, '//*[@id="state"]/div/div[1]/div[1]')
    SELECT_CITY = (By.XPATH, '//div[@id="city"]')
    INPUT_CITY = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    CITY_TEXT = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')


    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')