# Prática 5: Configuração do Systemd e Controle de Versão com Git

Este repositório contém os arquivos e a documentação da Prática 5 da disciplina SEL0337 - Projetos em Sistemas Embarcados, focada na criação de serviços de inicialização com `systemd` e no versionamento de código com Git/GitHub.

## Parte 1: Serviço de Inicialização com Systemd

### Resumo do Funcionamento do Projeto

O objetivo desta parte foi criar um serviço que inicia automaticamente um programa em Python durante o boot da Raspberry Pi, sem a necessidade de login manual.

Para isso, foi utilizado o `systemd`, o gerenciador de serviços padrão do Linux, para gerenciar um script Python que pisca um LED.

### Implementação

O processo foi dividido nas seguintes etapas:

1.  **Criação dos Scripts Python:**
    * **`blink.py`**: Script principal que utiliza a biblioteca `gpiozero` para controlar a GPIO 18, criando um loop infinito que acende e apaga um LED.
    * **`blink_off.py`**: Script auxiliar que apenas desliga o LED. Este script é essencial para a diretiva `ExecStop`, garantindo que o pino GPIO seja liberado corretamente quando o serviço é parado.

2.  **Criação do Arquivo de Serviço (`pyblink.service`):**
    * Foi criado um arquivo `unit file` para instruir o `systemd` sobre como gerenciar o script.
    * `[Unit]`: Define a descrição do serviço.
    * `[Service]`:
        * `ExecStart`: Especifica o comando para iniciar o serviço (ex: `/usr/bin/python3 /caminho/para/blink.py`).
        * `ExecStop`: Especifica o comando para parar o serviço (ex: `/usr/bin/python3 /caminho/para/blink_off.py`).
        * A linha `user=` define o usuario como "SEL".
    * `[Install]`:
        * `WantedBy=multi-user.target`: Garante que o serviço seja carregado durante o boot padrão do sistema.

3.  **Instalação e Teste do Serviço:**
    * O serviço foi copiado para `/lib/systemd/system/`.
    * Os comandos `systemctl daemon-reload`, `systemctl start` e `systemctl stop` foram usados para testar o serviço.
    * Finalmente, o comando `systemctl enable` foi usado para habilitar o serviço na inicialização.

### Montagem Prática

O circuito utilizado consiste em um LED conectado à **GPIO 18** da Raspberry Pi, com um resistor de 330 $\Omega$ para limitar a corrente.

> **(COLOQUE SUA FOTO DA MONTAGEM AQUI)**
> 

### Verificação do Funcionamento

O serviço foi verificado reiniciando a Raspberry Pi (`sudo reboot`). Conforme esperado, o LED começou a piscar automaticamente assim que o sistema operacional foi carregado, confirmando que o serviço `systemd` foi executado com sucesso no boot.

> **(COLOQUE SEU PRINT SCREEN OU FOTO DO LED PISCANDO AQUI)**
> 

## Parte 2: Arquivos do Projeto

Este repositório contém os seguintes arquivos exigidos pela prática:

* **`blink.py`**: Script Python principal (comentado).
* **`blink_off.py`**: Script Python de parada (comentado).
* **`pyblink.service`**: Arquivo de serviço do systemd (comentado).
* **`historico_git.txt`**: Log de commits gerado pelo comando `git log`.
* **`README.md`**: Este arquivo de documentação.
