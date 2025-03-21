import allure
import pytest
from ui.pages.kinopoisk_search_page import KinopoiskSearchPage
from config.settings import Settings


@allure.feature("Поиск фильма")
@allure.story("Поиск фильма по названию")
def test_search_movie_by_title(driver):
    search_page = KinopoiskSearchPage(driver)

    with allure.step("Открыть страницу поиска"):
        search_page.open_search_page()

    with allure.step("Закрыть модальное окно если есть"):
        search_page.close_modal()

    with allure.step("Поиск по полному названию"):
        search_page.search_movie_by_phrase("Интерстеллар")

    with allure.step("Проверить результаты поиска"):
        assert "Интерстеллар" in search_page.get_first_movie_title("258687")
