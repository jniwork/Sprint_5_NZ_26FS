class Locators:
    # Registration page
    REGISTRATION_INPUT_NAME = '//input[@name="name"]'
    REGISTRATION_INPUT_EMAIL = '//fieldset[2]//input[@name="name"]'
    REGISTRATION_INPUT_PASSWORD = '//input[@type="password"]'
    REGISTRATION_BUTTON = '//button[text()="Зарегистрироваться"]'
    REGISTRATION_PAGE_LOGIN_BUTTON = '//a[text()="Войти"]'
    REGISTRATION_INVALID_PASSWORD_MESSAGE = '//p[text()="Некорректный пароль"]'

    # Login page
    LOGIN_MAIN_PAGE_BUTTON = '//button[text()="Войти в аккаунт"]'
    LOGIN_INPUT_EMAIL = '//input[@name="name"]'
    LOGIN_INPUT_PASSWORD = '//input[@name="Пароль"]'
    LOGIN_PAGE_LOGIN_BUTTON = '//button[text()="Войти"]'

    # Account page
    ACCOUNT_PAGE_LOGIN_BUTTON = '//button[text()="Войти"]'
    ACCOUNT_PAGE_LOGOUT_BUTTON = '//button[text()="Выход"]'

    # Forgot password page
    FORGOT_PASSWORD_PAGE_LOGIN_BUTTON = '//a[text()="Войти"]'

    # Main page
    MAIN_PAGE_ACCOUNT_BUTTON = '//p[text()="Личный Кабинет"]'
    MAIN_PAGE_CONSTRUCTOR_BUTTON = '//p[text()="Конструктор"]'
    MAIN_PAGE_HEADER = '//h1[text()="Соберите бургер"]'
    MAIN_PAGE_LOGO = '//div[contains(@class, "AppHeader_header__logo")]'
    MAIN_PAGE_BREADS = '//span[text()="Булки"]/parent::div'
    MAIN_PAGE_SAUCES = '//span[text()="Соусы"]/parent::div'
    MAIN_PAGE_TOPPINGS = '//span[text()="Начинки"]/parent::div'
    MAIN_PAGE_ACTIVE_TAB = '//div[contains(@class, "tab_tab_type_current")]//span'
