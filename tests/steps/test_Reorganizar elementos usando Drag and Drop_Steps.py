from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/Reorganizar elementos usando Drag and Drop.feature')


@given('que eu acesso o site "https://demoqa.com/"')
def acessar_site(browser: Page):
    browser.set_viewport_size({"width": 1024, "height": 900})
    browser.goto('https://demoqa.com/')


@when('eu escolho a opção "Interactions" na página inicial e clico no submenu "Sortable"')
def escolho_opcoes(browser: Page):
    browser.get_by_text('Interactions', exact=True).click()
    browser.get_by_text('Sortable', exact=True).click()


@when('eu utilizo o método de drag and drop para ordenar os elementos de forma crescente')
def utilizo_metodo_drag_and_drop(browser: Page):
    lista_elementos = browser.locator("#demo-tabpane-list .list-group-item")
    total_itens = lista_elementos.count()

    for i in range(total_itens - 1):
        elemento_atual = lista_elementos.nth(i)
        proximo_elemento = lista_elementos.nth(i + 1)

        # Arrasta o elemento atual para a posição do próximo (ordenação crescente)
        elemento_atual.drag_to(proximo_elemento)


@then('eu valido que os elementos estão na ordem correta')
def valido_elementos_ordenados(browser: Page):
    lista_elementos = browser.locator("#demo-tabpane-list .list-group-item")
    texto_elementos = [lista_elementos.nth(i).inner_text() for i in range(lista_elementos.count())]

    ordem_esperada = ["One", "Two", "Three", "Four", "Five", "Six"]

