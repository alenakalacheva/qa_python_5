
from locators import Locators
from urls import Urls
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    def test_registration_successful(self, driver):
        email = f'alenakalacheva_5_{str(random.randint(100, 999))}@gmail.ru'
        driver = driver
        driver.get(Urls.REGISTRATION_URL)
        driver.find_element(*Locators.NAME_INPUT).send_keys('Sam')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.PROFILE_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_INPUT))

        assert driver.find_element(*Locators.LOGIN_INPUT).get_attribute('value') == email

    def test_registration_short_password(self, driver):
        email = f'alenakalacheva_5_{str(random.randint(100, 999))}@gmail.ru'
        driver = driver
        driver.get(Urls.REGISTRATION_URL)
        driver.find_element(*Locators.NAME_INPUT).send_keys('Sam')
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert driver.find_element(*Locators.WRONG_PASSWORD)
