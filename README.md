# qa_python_5
## UI автотесты для Stellar Burgers

### test_authorization - Проверка авторизации
* test_auth_main_page - Авторизация с главной страницы
* test_auth_profile_button - Авторизация по кнопке Личный кабинет
* test_auth_registration_page - Авторизация со страницы регистрации
* test_auth_recover_password - Авторизация со страницы востановления пароля
### test_constructor - Проверка конструктора
* test_switch_sauce - Переход на вкладку с соусами
* test_switch_filling - Переход на вкладку с начинками
* test_switch_buns - Переход на вкладку с булками
### test_profile_page - Проверка личного кабинета
* test_follow_profile_button - Переход в личный кабинет
* test_follow_constructor_button Переход в конструктор из Личного кабинета
* test_follow_logo - Переход в конструктор по логотипу
* test_logout - Выход из аккаунта
### test_registration - Проверка регистрации пользователя
* test_registration_successful - Проверка регистрации пользователя
* test_registration_short_password - Проверка сообщения о некорректном пароле

**auth_info** - данные для авторизации
**conftest** - фикстуры
**locators** - локаторы элементов
**urls** - url-адреса

*Для запуска тестов нужны **pytest** и **selenium***
