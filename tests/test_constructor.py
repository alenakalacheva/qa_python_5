from locators import Locators
from urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor:
    def test_switch_sauce(self, driver):
        driver = driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.INGREDIENTS_LIST))
        driver.find_element(*Locators.SAUCE_BUTTON).click()

        assert "current" in driver.find_element(*Locators.SAUCE_BUTTON).get_attribute("class")

    def test_switch_filling(self, driver):
        driver = driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.INGREDIENTS_LIST))
        driver.find_element(*Locators.FILLING_BUTTON).click()

        assert "current" in driver.find_element(*Locators.FILLING_BUTTON).get_attribute("class")

    def test_switch_buns(self, driver):
        driver = driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.INGREDIENTS_LIST))
        driver.find_element(*Locators.FILLING_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()

        assert "current" in driver.find_element(*Locators.BUNS_BUTTON).get_attribute("class")
