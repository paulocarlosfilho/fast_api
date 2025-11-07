#!/bin/bash

# Verifica se o Poetry já está instalado
if command -v poetry &> /dev/null
then
    echo "Poetry já está instalado."
else
    echo "Instalando Poetry..."
    # Instala o Poetry (método oficial para Linux/WSL)
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Adiciona o diretório binário do Poetry ao PATH (necessário para rodar o poetry)
    if [[ ":$PATH:" != *":$POETRY_BIN:"* ]]; then
        export PATH="$POETRY_BIN:$PATH"
        echo "PATH atualizado para incluir o binário do Poetry."
    fi
fi

# Verifica a instalação
poetry --version || { echo "❌ Falha na instalação do Poetry. Abortando."; exit 1; }

echo "--- 2. Instalação de Dependências com Poetry ---"

# Cria o ambiente virtual e instala as dependências

# Usamos `poetry add` para garantir que `pyproject.toml` e `poetry.lock` sejam criados/atualizados
poetry add fastapi uvicorn
echo "FastAPI e Uvicorn adicionados e instalados."

# echo "--- 3. Configuração do Git e Commit ---"

# Configura o helper de credenciais (se não estiver globalmente)
# git config --global credential.helper store

# git config --global user.email # Ou algo assim
# git config --global user.user

# Adiciona todos os arquivos (incluindo as mudanças do Poetry)
git add .
echo "Todos os arquivos adicionados, incluindo as mudanças do Poetry."

# Renomeia o branch local para 'main'
git branch -M main
echo "Branch local renomeado para 'main'."

