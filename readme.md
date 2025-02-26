# Discord Bot

Este é um bot do Discord que formata mensagens para serem usadas em queries SQL.

## Requisitos

- Python 3.13
- discord.py 2.3.2
- python-dotenv 0.9.9

## Instalação

Crie um arquivo [.env]baseado no [.env.example] e adicione o seu token  Discord:
    ```
    DISCORD_TOKEN='seu_token_aqui'
    ```

## Uso

1. Execute o bot:
    ```sh
    python [main.py]
    ```
2. No Discord, use os seguintes comandos:
    - `!ping`: Verifica a latência do bot.
    - `!ajuda`: Envia uma mensagem de ajuda para o usuário.
    - `!f itens`: Envia o texto formatado.