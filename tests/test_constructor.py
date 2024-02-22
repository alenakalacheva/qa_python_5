from locators import Locators
from urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestConstructor:
    def test_switch_sauce(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        driver.find_element(*Locators.SAUCE_BUTTON).click()

        time.sleep(2)
        position = driver.find_element(*Locators.SAUCE_LABEL).rect

        assert (int(position['y']) == 243 and
                "current" in driver.find_element(*Locators.SAUCE_BUTTON).get_attribute("class"))

    def test_switch_filling(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        driver.find_element(*Locators.FILLING_BUTTON).click()

        time.sleep(2)
        position = driver.find_element(*Locators.FILLING_LABEL).rect

        assert (int(position['y']) == 243 and
                "current" in driver.find_element(*Locators.FILLING_BUTTON).get_attribute("class"))

    def test_switch_buns(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        driver.find_element(*Locators.FILLING_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        time.sleep(2)
        position = driver.find_element(*Locators.BUNS_LABEL).rect

        assert (int(position['y']) == 243 and
                "current" in driver.find_element(*Locators.BUNS_BUTTON).get_attribute("class"))
