import csv
import os
from flask import Flask, render_template

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

# Teste de Glossário
glossario = [
    ['Internet', 'Acessar internet'],
    ['Java', 'Pior linguagem de Programação'],
    ['Python', 'Melhor linguagem']
             ]

@app.route('/')
def ola():
    return render_template('index.html', glossario=glossario)


@app.route('/sobre-equipe')
def sobre():
    return render_template('sobre.html')

@app.route('/glossario')
def glossario():

    glossario_termos = []
    with open(
        'bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_termos.append(l)
            return render_template(
                'glossario.html', glossario=glossario_termos
            )
@app.route('/novo_termo')
def novo_termo():
    return render_template('adicionar_termo.html')


if __name__ == "__main__":
    app.run(debug=True)
