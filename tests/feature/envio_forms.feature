Feature: Preenchimento do formulário no site DemoQA

  Scenario: Preencher e submeter o formulário corretamente
    Given que o usuário acessa o site "https://demoqa.com/"
    When o usuário seleciona a opção "Forms" na página inicial
    And o usuário clica no submenu "Practice Form" preenche todos os campos do formulário com valores aleatórios
    Then o usuário fecha o popup
