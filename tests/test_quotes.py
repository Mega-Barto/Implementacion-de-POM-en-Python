# tests/test_pages.py

import pytest

def test_page_load(quotes_page):
    """Prueba básica para verificar que la página carga correctamente."""
    assert "Quotes" in quotes_page.driver.title, "La página de citas no cargó correctamente"

def test_quotes_extraction(quotes_page):
    """Prueba que verifica la extracción de citas en la página de citas."""
    quotes = quotes_page.get_quotes()
    assert len(quotes) > 0, "No se encontraron citas en la página"
    for quote in quotes:
        assert len(quote) > 0, "El texto de la cita no debe estar vacío"

def test_authors_extraction(quotes_page):
    """Prueba que verifica la extracción de autores en la página de citas."""
    authors = quotes_page.get_authors()
    assert len(authors) > 0, "No se encontraron autores en la página"
    for author in authors:
        assert len(author) > 0, "El nombre del autor no debe estar vacío"

def test_navigation_to_next_page(quotes_page):
    """Prueba que verifica la navegación a la página siguiente."""
    # Si tienes un método en `quotes_page` llamado `go_to_next_page`
    quotes_page.go_to_next_page()
    assert "page/2" in quotes_page.driver.current_url, "La navegación a la siguiente página falló"

def test_quotes_content(quotes_page):
    """Prueba que verifica el contenido de una cita específica."""
    # Si esperas un contenido específico para validar
    expected_quote = '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
    quotes = quotes_page.get_quotes()
    assert expected_quote in quotes, f"No se encontró la cita esperada: '{expected_quote}'"

def test_author_presence(quotes_page):
    """Prueba que verifica la presencia de un autor específico."""
    # Si esperas un autor específico para validar
    expected_author = "Albert Einstein"
    authors = quotes_page.get_authors()
    assert expected_author in authors, f"No se encontró el autor esperado: '{expected_author}'"
