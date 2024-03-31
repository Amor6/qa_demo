import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name = 'Ivan'
        last_name = 'Ivanov'
        email = 'name@example.com'
        number = '7777777777'
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(number)
        self.element_is_visible(Locators.DATE_OF_BIRTH).get_attribute('value')
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('Biology')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r'C:\Project\test_selenium\dk.png')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('MSK, home 50')
        self.element_is_visible(Locators.SELECT_STATE).click()
        self.element_is_visible(Locators.INPUT_STATE).send_keys(Keys.RETURN)
        self.element_is_visible(Locators.SELECT_CITY).click()
        self.element_is_visible(Locators.INPUT_CITY).send_keys(Keys.RETURN)
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()
        time.sleep(5)
