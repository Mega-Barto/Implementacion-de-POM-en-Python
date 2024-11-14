# conftest.py

import pytest
from selenium import webdriver
from pages.quotes_page import QuotesPage  # Ajusta la importación según tu estructura
from config.config import Config

@pytest.fixture
def driver():
    # Configura el controlador de Selenium (en este caso, Chrome)
    driver = webdriver.Firefox()  # Asegúrate de que ChromeDriver esté en tu PATH o especifica la ruta
    driver.implicitly_wait(10)   # Configuración de espera implícita
    yield driver
    driver.quit()  # Cierra el navegador después de cada prueba

@pytest.fixture
def quotes_page(driver):
    # Inicializa y abre la página de citas
    page = QuotesPage(driver)
    page.open(Config.BASE_URL)  # Abre la URL base establecida en QuotesPage
    return page
