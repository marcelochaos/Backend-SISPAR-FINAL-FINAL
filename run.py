# SUA UNICA FUNCIONALIDADE É INICIAR O NOSSO SERVIDOR

from src.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)