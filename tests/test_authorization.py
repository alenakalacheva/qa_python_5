from locators import Locators
from urls import Urls
from auth_info import AuthInfo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorization:
    def test_auth_main_page(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_auth_profile_button(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_auth_registration_page(self, get_driver):
        driver = get_driver
        driver.get(Urls.REGISTRATION_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.REGISTRATION_BUTTON))

        driver.find_element(*Locators.LOGIN_URL).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_auth_recover_password(self, get_driver):
        driver = get_driver
        driver.get(Urls.RECOVER_PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.RECOVER_BUTTON))

        driver.find_element(*Locators.LOGIN_URL).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON)

