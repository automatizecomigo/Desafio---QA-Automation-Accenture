from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/Teste do Progress Bar.feature')



@given('que eu acesso o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('eu escolho a opção "Widgets" na página inicial e clico no submenu "Progress Bar" e clico no botão "Start" '
      'e paro a progress bar antes dos 25%')
def selecionar_opcoes_seleciono_progress_bar(browser: Page):
    browser.get_by_text('Widgets',exact=True).click()
    browser.get_by_text('Progress Bar',exact=True).click()
    browser.get_by_text('Start',exact=True).click()
    while True:
        progresso_Bar = browser.locator("#progressBar > div").get_attribute("aria-valuenow")
        progress_value = int(progresso_Bar ) if progresso_Bar  else 0

        if progress_value >= 25:
            browser.get_by_text('Stop', exact=True).click()
            break

@then('eu valido que o valor da progress bar é menor ou igual a 25%')
def validor_progress_bar(browser: Page):
    expect(browser.get_by_text('25%',exact=True))

@when('eu aperto "Start" novamente e aguardo até a barra atingir 100%')
def validor_progress_bar(browser: Page):
    browser.get_by_text('Start',exact=True).click()

    while True:
        progresso_Bar = browser.locator("#progressBar > div").get_attribute("aria-valuenow")
        progress_value = int(progresso_Bar ) if progresso_Bar  else 0
        if progress_value >= 100:
            break


@then('eu reseto a progress bar')
def reseto_progress_bar(browser: Page):
    browser.get_by_text('Reset',exact=True).click()