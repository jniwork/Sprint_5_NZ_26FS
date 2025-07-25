class Locators:
    # Registration page
    REGISTRATION_INPUT_NAME = '(//input[@name="name"])[1]'
    REGISTRATION_INPUT_EMAIL = '(//input[@name="name"])[2]'
    REGISTRATION_INPUT_PASSWORD = '//input[@type="password"]'
    REGISTRATION_BUTTON = '//button[contains(text(), "Зарегистрироваться")]'
    REGISTRATION_PAGE_LOGIN_BUTTON = '//a[contains(text(), "Войти")]'
    REGISTRATION_INVALID_PASSWORD_MESSAGE = '//p[contains(text(), "Некорректный пароль")]'

    # Login page
    LOGIN_MAIN_PAGE_BUTTON = '//button[contains(text(), "Войти в аккаунт")]'
    LOGIN_INPUT_EMAIL = '//input[@name="name"]'
    LOGIN_INPUT_PASSWORD = '//input[@name="Пароль"]'
    LOGIN_PAGE_LOGIN_BUTTON = '//button[contains(text(), "Войти")]'

    # Account page
    ACCOUNT_PAGE_LOGIN_BUTTON = '//button[contains(text(), "Войти")]'
    ACCOUNT_PAGE_LOGOUT_BUTTON = '//button[contains(text(), "Выход")]'

    # Forgot password page
    FORGOT_PASSWORD_PAGE_LOGIN_BUTTON = '//a[contains(text(), "Войти")]'

    # Main page
    MAIN_PAGE_ACCOUNT_BUTTON = '//p[contains(text(), "Личный Кабинет")]'
    MAIN_PAGE_CONSTRUCTOR_BUTTON = '//p[contains(text(), "Конструктор")]'
    MAIN_PAGE_HEADER = '//h1[contains(text(), "Соберите бургер")]'
    MAIN_PAGE_LOGO = "//div[@class='AppHeader_header__logo__2D0X2']"
    MAIN_PAGE_BREADS = "//span[text()='Булки']/parent::div"
    MAIN_PAGE_SAUCES = "//span[text()='Соусы']/parent::div"
    MAIN_PAGE_TOPPINGS = "//span[text()='Начинки']"
    MAIN_PAGE_ACTIVE_TAB = "//div[contains(@class, 'tab_tab_type_current')]"
