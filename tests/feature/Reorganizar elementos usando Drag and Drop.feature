Feature: Reorganizar elementos usando Drag and Drop no DemoQA

  Scenario: Ordenar elementos na página Sortable
    Given que eu acesso o site "https://demoqa.com/"
    When eu escolho a opção "Interactions" na página inicial e clico no submenu "Sortable"
    And eu utilizo o método de drag and drop para ordenar os elementos de forma crescente
    Then eu valido que os elementos estão na ordem correta
