from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KinopoiskLoginPage(BasePage):
    # Поле для ввода номера телефона
    PHONE_INPUT = (By.XPATH, "//input[@id='passp-field-phone']")
    # Кнопка войти и "Отправить код"
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='passp:sign-in' and @data-t='button:action:passp:sign-in']")
    # Поле для ввода кода из push-уведомления
    CODE_INPUT = (By.XPATH, "//input[@id='passp-field-phoneCode']")
    PROFILE_SELECTION = (By.CSS_SELECTOR, ".AccountsListItem-login")  # Блок выбора профиля
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_loginButton__LWZQp') and text()='Войти']")    # Кнопка войти в профиль
    CLOSE_MODAL = (By.CSS_SELECTOR,"[data-tid='d6ef5dc']")
    AVATAR_PIC = (By.CSS_SELECTOR,"[data-tid='15bd9013']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open_login_page(self):
        self.driver.get("https://www.kinopoisk.ru/")

    def close_modal(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CLOSE_MODAL)
        ).click()

    def click_login_button(self):
        """Нажатие кнопки 'войти в профиль'."""
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def enter_phone_number(self, phone_number):
        """
        Ввод номера телефона.

        :param phone_number: Номер телефона для входа.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.PHONE_INPUT)
        ).send_keys(phone_number)

    def submit_phone_number(self):
        """Нажатие кнопки 'войти'."""
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)

        # Нажать кнопку
        submit_button.click()


    def select_profile(self, profile_name):
        """
        Выбор профиля
        """
        self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_SELECTION)
        ).click()

    def is_logged_in(self):
        """Проверка, что пользователь авторизован."""
        try:
            self.wait.until(EC.presence_of_element_located(self.AVATAR_PIC))
            return True
        except:
            return False
