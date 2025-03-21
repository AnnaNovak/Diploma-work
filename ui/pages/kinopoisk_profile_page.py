from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KinopoiskProfilePage(BasePage):
    BOOKMARKS_SECTION = (By.XPATH, "//a[contains(text(), 'Закладки')]")
    BOOKMARKED_MOVIES = (By.CLASS_NAME, "bookmarked-movie")

    def __init__(self, driver):
        super().__init__(driver)

    def open_bookmarks(self):
        self.click(self.BOOKMARKS_SECTION)

    def get_bookmarked_movies(self):
        return self.driver.find_elements(*self.BOOKMARKED_MOVIES)