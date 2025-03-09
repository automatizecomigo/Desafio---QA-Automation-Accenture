Feature: Interagir com Web Tables no site demoqa.com

  Scenario: Criar, editar e deletar um registro
    Given Eu acesso o site "https://demoqa.com/"
    When Eu escolho a opção "Elements" na página inicial Eu clico no submenu "Web Tables"
    And Eu crio um novo registro e valido
    And Eu edito o novo registro criado e valido
    And Eu deleto o novo registro criado

  Scenario: Criar e deletar múltiplos registros dinamicamente
    Given Eu acesso o site "https://demoqa.com/"
    When Eu escolho a opção "Elements" na página inicial Eu clico no submenu "Web Tables"
    And Eu crio 12 novos registros de forma dinâmica
    Then Eu deleto todos os 12 novos registros criados
