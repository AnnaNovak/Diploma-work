import allure
from ui.pages.kinopoisk_login_page import KinopoiskLoginPage
from config.settings import Settings


@allure.feature("UI Тесты")
@allure.story("Авторизация на Кинопоиске")
def test_kinopoisk_login(driver):
    login_page = KinopoiskLoginPage(driver)

    with allure.step("Открыть страницу входа"):
        login_page.open_login_page()

    with allure.step("Закрыть модальное окно если есть"):
        login_page.close_modal()

    with allure.step("Нажать кнопку 'войти'"):
        login_page.click_login_button()

    with allure.step("0000000000"): # ввести свой номер телефона
        login_page.enter_phone_number(Settings.USER_PHONE)

    with allure.step("Нажать кнопку 'Войти'"):
        login_page.submit_phone_number()

    with allure.step("Выбрать профиль 'Мой профиль'"):
        login_page.select_profile("Мой профиль")

    with allure.step("Проверить, что пользователь авторизован"):
        assert login_page.is_logged_in(), "Пользователь не авторизован"
