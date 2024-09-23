from flask import Flask, request, render_template
from weasyprint import HTML
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gerar_pdf', methods=['POST'])
def gerar_pdf():
    titulo = request.form['titulo']
    conteudo = request.form['conteudo']

    # Criar o HTML para o PDF
    html = f"""
    <html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <img src="logo.png" alt="Logo" style="width: 100px;"/>
            <h1>{titulo}</h1>
        </header>
        <p>{conteudo}</p>
    </body>
    </html>
    """

    # Gerar o PDF
    pdf = HTML(string=html).write_pdf()
    with open('documento_gerado.pdf', 'wb') as f:
        f.write(pdf)

    return "PDF gerado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
