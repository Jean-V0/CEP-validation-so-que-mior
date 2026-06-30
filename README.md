# CEP-validation

## Como usar com Poetry e venv

Este projeto já está preparado para usar uma virtualenv local em `.venv` e o Poetry para gerenciar dependências.

### 1) Criar e ativar a venv

```bash
cd /home/jean/projetos/CEP-validation-so-que-mior
python -m venv .venv
source .venv/bin/activate
```

### 2) Instalar Poetry dentro da venv

```bash
python -m pip install --upgrade pip
python -m pip install poetry
```

### 3) Instalar dependências do projeto

```bash
poetry install
```

### 4) Rodar o script

```bash
poetry run python main.py
```

### 5) Se quiser usar só a venv sem Poetry

```bash
source .venv/bin/activate
pip install pandas requests openpyxl
python main.py
```

## Ferramentas utilizadas:

- Python: 3.14.6^
- Poetry
- Python-venv

### Obs: Todas as libs foram centralizadas no poetry para dar menos dor de cabeça. Os 1 - 5 é um passo a passo que peguei da IA caso não saiba usar venv e poetry