from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
    pagina.locator('xpath=//*[@id="firstname"]').click()
    pagina.fill('xpath=//*[@id="firstname"]', "André")
    pagina.fill('xpath=// *[ @ id = "email"]', "andre@teste.com")
    pagina.fill('xpath=//*[@id="phone"]', "99 99999999")
    pagina.locator('xpath=//*[@id="_form_2475_submit"]').click()

    time.sleep(5)