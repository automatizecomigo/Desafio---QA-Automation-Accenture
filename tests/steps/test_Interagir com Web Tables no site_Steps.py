from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/Interagir com Web Tables no site.feature')



@given('Eu acesso o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('Eu escolho a opção "Elements" na página inicial Eu clico no submenu "Web Tables"')
def selecionar_opcoes(browser: Page):
    browser.get_by_text('Elements',exact=True).click()
    browser.get_by_text('Web Tables',exact=True).click()

@when('Eu crio um novo registro e valido')
def criar_novo_registro(browser: Page):
    browser.get_by_text('Add',exact=True).click()
    browser.locator('[placeholder="First Name"]').fill('Rafael')
    browser.locator('[placeholder="Last Name"]').fill('Pantoja')
    browser.locator('[placeholder="name@example.com"]').fill('automatizecomigo@gmail.com')
    browser.locator('[placeholder="Age"]').fill('33')
    browser.locator('[placeholder="Salary"]').fill('5000')
    browser.locator('[placeholder="Department"]').fill('QA Pleno')
    browser.locator('[type="submit"]').click()
    expect(browser.get_by_text('Rafael',exact=True))


@when('Eu edito o novo registro criado e valido')
def editor_novo_registro(browser: Page):
    browser.locator('#edit-record-4 path').click()
    browser.locator('[placeholder="First Name"]').fill('Rafael-Editado')
    browser.locator('[type="submit"]').click()

@when('Eu deleto o novo registro criado')
def deletar_novo_registro(browser: Page):
    browser.locator('#delete-record-4 path').click()


@given('Eu acesso o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('Eu escolho a opção "Elements" na página inicial Eu clico no submenu "Web Tables"')
def selecionar_opcoes(browser: Page):
    browser.get_by_text('Elements',exact=True).click()
    browser.get_by_text('Web Tables',exact=True).click()

@when('Eu crio 12 novos registros de forma dinâmica')
def criar_novos_registros(browser: Page):
    for i in range(1, 13):  # Loop para criar 12 registros
        browser.get_by_text('Add', exact=True).click()
        browser.locator('[placeholder="First Name"]').fill(f'Rafael{i}')
        browser.locator('[placeholder="Last Name"]').fill(f'Pantoja{i}')
        browser.locator('[placeholder="name@example.com"]').fill(f'automatizecomigo{i}@gmail.com')
        browser.locator('[placeholder="Age"]').fill('33')
        browser.locator('[placeholder="Salary"]').fill('5000')
        browser.locator('[placeholder="Department"]').fill('QA Pleno')
        browser.locator('[type="submit"]').click()
        expect(browser.get_by_text(f'Rafael{i}', exact=True))


@then('Eu deleto todos os 12 novos registros criados')
def deletar_todos_registros(browser: Page):
    for i in range(1, 13):
        browser.locator(f'#delete-record-{i} path').click()
        browser.wait_for_selector(f'#delete-record-{i}', state='detached')