# Sprint_5

## Что нужно проверить

### Регистрация
Проверь:
Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
Ошибку для некорректного пароля. 
>test_successful_registration, test_unsuccessful_registration
### Вход
Проверь:
1. вход по кнопке «Войти в аккаунт» на главной
> test_login_from_main_page
2. вход через кнопку «Личный кабинет»,
> test_login_from_account_page
3. вход через кнопку в форме регистрации,
> test_login_from_registration_page
3. вход через кнопку в форме восстановления пароля.
> test_login_from_forgot_password_page
### Переход в личный кабинет 
Проверь переход по клику на «Личный кабинет».
> test_transition_to_account
### Переход из личного кабинета в конструктор 
Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
> test_transition_to_constructor, test_transition_to_constructor_from_logo

### Выход из аккаунта
Проверь выход по кнопке «Выйти» в личном кабинете.
> test_logout_from_account_page
### Раздел «Конструктор»
Проверь, что работают переходы к разделам:
1. «Булки»,
> test_transition_to_tab_breads
2. «Соусы»,
> test_transition_to_tab_sauces
3. «Начинки».
> test_transition_to_tab_toppings