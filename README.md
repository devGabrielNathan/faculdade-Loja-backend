README para o Backend (Django com Django REST Framework)
Django REST API
Este é o backend da aplicação, desenvolvido em Django utilizando o Django REST Framework (DRF) para criar uma REST API.

Requisitos
Python instalado na máquina (recomendado Python 3.8+)
SQLite instalado
Virtualenv instalado
Visual Studio Code (VSCode) com as extensões Python e SQLite
Instalação
Passo 1: Instalar Python
Certifique-se de que o Python está instalado na sua máquina. Para verificar, abra o terminal e execute:

bash
Copiar código
python --version
Se o Python não estiver instalado, faça o download e instale a partir de python.org.

Passo 2: Instalar SQLite
macOS
O SQLite já vem pré-instalado no macOS.

Linux
Execute o seguinte comando no terminal:

bash
Copiar código
sudo apt-get install sqlite3
Windows
Baixe o SQLite a partir de sqlite.org/download.html e siga as instruções de instalação.

Passo 3: Instalar a extensão SQLite no VSCode
Instale a extensão "SQLite" no VSCode a partir do marketplace de extensões do VSCode.

Passo 4: Criar e ativar um ambiente virtual
macOS / Linux
Crie um ambiente virtual:
bash
Copiar código
python -m venv env
Ative o ambiente virtual:
bash
Copiar código
source env/bin/activate
Windows
Crie um ambiente virtual:
bash
Copiar código
python -m venv env
Ative o ambiente virtual:
bash
Copiar código
.\env\Scripts\activate
Passo 5: Instalar dependências
Após ativar o ambiente virtual, instale as dependências da aplicação:

bash
Copiar código
pip install -r requirements.txt
Passo 6: Inicializar a aplicação
Para iniciar a aplicação backend, execute:

bash
Copiar código
python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.