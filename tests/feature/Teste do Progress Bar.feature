Feature: Teste do Progress Bar

  Scenario: Interagir com a barra de progresso e validar valores específicos
    Given que eu acesso o site "https://demoqa.com/"
    When eu escolho a opção "Widgets" na página inicial e clico no submenu "Progress Bar" e clico no botão "Start" e paro a progress bar antes dos 25%
    Then eu valido que o valor da progress bar é menor ou igual a 25%
    When eu aperto "Start" novamente e aguardo até a barra atingir 100%
    Then eu reseto a progress bar
