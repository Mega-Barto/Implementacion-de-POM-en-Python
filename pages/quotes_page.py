# pages/quotes_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class QuotesPage(BasePage):
    URL = "/"

    def open(self, url):
        # Construimos y pasamos la URL completa al método `open(url)` de BasePage
        full_url = Config.BASE_URL + self.URL
        super().open(full_url)  # Llamamos a `open` con `full_url`

    def get_quotes(self):
        quotes = self.find_elements(By.CLASS_NAME, "text")
        return [quote.text for quote in quotes]

    def get_authors(self):
        authors = self.find_elements(By.CLASS_NAME, "author")
        return [author.text for author in authors]
    
    def go_to_next_page(self):
        next_button = self.find_element(By.XPATH, "//li[@class='next']/a")
        next_button.click()