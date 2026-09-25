# baite

Um clipboard manager de terminal: fica observando sua área de transferência, guarda o histórico em `clips.json` e deixa você buscar e recarregar um clip antigo por um menu interativo.

## Pré-requisitos

- Python 3.12+
- `pip`
- Linux com um backend de clipboard disponível para o `pyperclip` (ex: `xclip` ou `xsel` no X11, ou Wayland com suporte equivalente)

## Rodando localmente

1. Clone o repositório e entre na pasta:

   ```bash
   git clone <url-do-repo>
   cd baitev2
   ```

2. Crie e ative um virtualenv:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o baite:

   ```bash
   python main.py
   ```

Ao iniciar, ele mostra a arte do gatinho, carrega o histórico salvo em `clips.json` e sobe uma thread em background observando a área de transferência. Todo texto novo copiado é salvo automaticamente. No menu:

- `[1]` busca um clip pelo termo digitado e permite recarregá-lo na área de transferência
- `[2]` encerra o programa

Para sair a qualquer momento, `Ctrl+C` também funciona.

## Próximos passos

- [ ] Criar um alias (`baite`) para executar o projeto direto do terminal sem precisar ativar o venv manualmente ou digitar `python main.py`.
