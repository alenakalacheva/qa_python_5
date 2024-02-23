from selenium.webdriver.common.by import By


class Locators:

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::div/input")  # Поле ввода имени пользователя
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']/parent::div/input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//label[text() = 'Пароль']/parent::div/input")  # поле ввода пароля
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка Зарегестрироваться

    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка Войти
    AUTHORIZATION_EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле ввода email (авторизация)
    AUTHORIZATION_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля (авторизация)

    PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка входа в личный кабинет

    LOGIN_INPUT = (By.XPATH, "//label[text() = 'Логин']/following-sibling::input")  # Поле логин в личном кабинете

    WRONG_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Некорректный пароль

    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    LOGIN_URL = (By.XPATH, "//a[text()='Войти']")

    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LOGO = (By.XPATH, ".//header//div/a[@href='/']")

    LOGOUT = (By.XPATH, ".//button[text()='Выход']")

    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCE_BUTTON = (By.XPATH, ".//span[text() = 'Соусы']/parent::div")
    FILLING_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    BUNS_LABEL = (By.XPATH, ".//h2[text()='Булки']")
    SAUCE_LABEL = (By.XPATH, ".//h2[text()='Соусы']")
    FILLING_LABEL = (By.XPATH, ".//h2[text()='Начинки']")
    INGREDIENTS_LIST = (By.XPATH, ".//ul[starts-with(@class, 'BurgerIngredient')]")






