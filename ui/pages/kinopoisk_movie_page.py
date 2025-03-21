from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KinopoiskMoviePage(BasePage):
    RATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Оценить')]")
    RATING_STARS = (By.CLASS_NAME, "rating-stars")
    ADD_TO_BOOKMARKS = (By.XPATH, "//button[contains(text(), 'В закладки')]")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")

    def __init__(self, driver):
        super().__init__(driver)

    def rate_movie(self, rating):
        self.click(self.RATE_BUTTON)
        self.click((By.XPATH, f"//div[@data-rating='{rating}']"))

    def add_to_bookmarks(self):
        self.click(self.ADD_TO_BOOKMARKS)

    def is_success_message_visible(self):
        return self.is_visible(self.SUCCESS_MESSAGE)