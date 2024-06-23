from selenium.webdriver.common.by import By


class Locators:
    # Поле "Имя"
    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле  "Email"
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль"
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Войти" при авторизации
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    # Вывод текста "Некорректный пароль"             ERROR_ что то там
    PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')
    # Кнопка "Войти в аккаунт" на главной странице
    MAIN_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    # Кнопка "Войти" в форме регистрации или восстановлении пароля
    LOGIN_BUTTON_FROM_REGISTER_OR_RESTORE_PASSWORD_FORM = (By.XPATH, '//a[text()="Войти"]')
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/" and .//p[text()="Конструктор"]]')
    # Логотип
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class,'logo')]/child::a")
    # Кнопка "Выход"
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    # Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div')
    # Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div')
    # Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div')
    # 1-на из начинок
    FILLING = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]')
    # 1 из соусов
    SAUCE = (By.XPATH, '//p[text()="Соус Spicy-X"]')
    # 1-на из булок
    BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')