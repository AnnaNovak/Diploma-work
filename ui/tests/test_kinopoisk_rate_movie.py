import allure
import pytest
from ui.pages.kinopoisk_movie_page import KinopoiskMoviePage

@allure.feature("Оценка фильма")
@allure.story("Пользователь может оценить фильм")
def test_rate_movie(driver):
    movie_page = KinopoiskMoviePage(driver)
    movie_page.rate_movie(rating=5)

    with allure.step("Проверить успешность оценки"):
        assert movie_page.is_success_message_visible()
