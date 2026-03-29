add lsp server setup:

```bash
uv tool install basedpyright
bun i -g vscode-langservers-extracted
```
- yaml-language-server
- vtsls
- https://github.com/tombi-toml/tombi
- bash-language-server

add uv setup:

```yaml
        - name: Set up Python
          uses: actions/setup-python@v5
          with:
              python-version: '3.12'

        - name: Install uv
          uses: astral-sh/setup-uv@v6
          with:
              enable-cache: true

        - name: Install GitHub CLI
          shell: bash
          run: |
              sudo apt-get update
              sudo apt-get install -y gh
```
