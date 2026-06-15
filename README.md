🚀 App Demonstrativo PyQt6
Este é um projeto simples de estudo desenvolvido em Python com PyQt6, demonstrando como manipular eventos de interface e exibir elementos visuais (imagens) dinamicamente.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Interface Gráfica: PyQt6

Gerenciamento de Eventos: Signals & Slots

📋 Como Executar
1. Pré-requisitos
Certifique-se de ter o Python 3 instalado em seu sistema Linux.

2. Configuração do Ambiente
Abra o terminal na pasta do projeto e execute os comandos abaixo:

Bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente
source venv/bin/activate

# Instalar PyQt6
pip install PyQt6
3. Execução
Certifique-se de que o arquivo botao_on.png esteja na mesma pasta do arquivo MinhaApp.py. Em seguida, execute:

Bash
python3 MinhaApp.py
💡 Funcionalidades
Carregamento Dinâmico: Ao clicar no botão "Mostrar Imagem", o programa tenta carregar e exibir o arquivo botao_on.png.

Tratamento de Erro: Caso o arquivo de imagem não seja encontrado, o aplicativo exibe uma mensagem de erro na interface em vez de travar.

Redimensionamento: A imagem é redimensionada automaticamente para caber no layout mantendo a proporção original.
