from pytest_bdd import given, when, then, scenarios 
from playwright.sync_api import expect, Page

scenarios('../feature/envio_forms.feature')



@given('que o usuário acessa o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('o usuário seleciona a opção "Forms" na página inicial')
def selecionar_forms(browser: Page):
    browser.get_by_text('Forms', exact=True).click()

@when('o usuário clica no submenu "Practice Form" preenche todos os campos do formulário com valores aleatórios')
def selecionar_forms(browser: Page):
    browser.get_by_text('Practice Form', exact=True).click()
    browser.locator('[placeholder="First Name"]').fill('Rafael')
    browser.locator('[placeholder="Last Name"]').fill('Pantoja')
    browser.locator('[placeholder="name@example.com"]').fill('automatizecomigo@gmail.com')
    browser.get_by_text('Male', exact=True).click()
    browser.locator('[placeholder="Mobile Number"]').fill('9983074577')
    browser.get_by_text('Sports', exact=True).click()

    browser.locator('#uploadPicture').set_input_files('c:/Users/USER/Desktop/Desafio Accenture/Playwright/imagens'
                                                      '/Accenture.jpg')
    browser.locator('#currentAddress').fill('Rua C 22 numero 1538 - Manaus - AM')
    browser.get_by_text('Select State', exact=True).click()
    browser.get_by_text("Haryana", exact=True).click()
    browser.get_by_text('Select City', exact=True).click()
    browser.get_by_text('Panipat', exact=True).click()
    browser.locator('[type="submit"]').click()



@then('o usuário fecha o popup')
def usuario_fecha_popup(browser: Page):
    browser.locator('role=button[name="Close"]').click()

