from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/Acessar e interagir com Alertas, Frames e Janelas.feature')



@given('Eu acesso o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('Eu escolho a opção "Alerts, Frame & Windows" na página inicial')
def selecionar_opcao(browser: Page):
    browser.get_by_text('Alerts, Frame & Windows',exact=True).click()

@when('Eu clico no submenu "Browser Windows" e clico no botao "New Window" devo ver uma janela aberta')
def selecionar_submenu(browser: Page):
    browser.get_by_text('Browser Windows',exact=True).click()
    browser.get_by_text('New Window',exact=True).click()
    expect(browser.get_by_text('This is a sample page',exact=True))

@then('Eu fecho a nova janela aberta')
def fechar_janela_ja_validada(browser: Page):
    browser.close()
