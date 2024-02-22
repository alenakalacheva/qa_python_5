from locators import Locators
from urls import Urls
from auth_info import AuthInfo
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#  Проверь переход по клику на «Личный кабинет».
class TestProfilePage:
    def test_follow_profile_button(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_INPUT))
        assert driver.find_element(*Locators.LOGIN_INPUT).get_attribute('value') == AuthInfo.EMAIL

    def test_follow_constructor_button(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_INPUT))

        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert driver.current_url == Urls.MAIN_URL

    def test_follow_logo(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_INPUT))

        driver.find_element(*Locators.LOGO).click()

        assert driver.current_url == Urls.MAIN_URL

    def test_logout(self, get_driver):
        driver = get_driver
        driver.get(Urls.MAIN_URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN))

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        driver.find_element(*Locators.AUTHORIZATION_EMAIL_INPUT).send_keys(AuthInfo.EMAIL)
        driver.find_element(*Locators.AUTHORIZATION_PASSWORD_INPUT).send_keys(AuthInfo.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ORDER_BUTTON))

        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_INPUT))

        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.LOGIN_BUTTON))

        assert driver.current_url == Urls.AUTHORIZATION_URL







#  Проверь переход по клику на «Конструктор»

#  и на логотип Stellar Burgers.


#  Проверь выход по кнопке «Выйти» в личном кабинете.
