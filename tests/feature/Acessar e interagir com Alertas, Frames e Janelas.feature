Feature: Acessar e interagir com Alertas, Frames e Janelas

  Scenario: Abrir nova janela e validar a mensagem
    Given Eu acesso o site "https://demoqa.com/"
    When Eu escolho a opção "Alerts, Frame & Windows" na página inicial
    And Eu clico no submenu "Browser Windows" e clico no botao "New Window" devo ver uma janela aberta
    Then Eu fecho a nova janela aberta