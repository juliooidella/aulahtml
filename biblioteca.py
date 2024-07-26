from flask import Flask

app = Flask(__name__)

@app.route("/inicio")
def inicio():
    return ("<h1> Titulo do meu Site</h1> <p>Este é um paragrafo</p>")

@app.route("/lista")
def listar_livros():
    return """  <!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="bootstrap.css" />
        <title>
            Biblioteca Senai
        </title>
    </head>
    <body>
        <h1>Lista de Livros</h1>
        <p>Página para listar os Livros da Biblioteca do Senai</p>

        <table class="table table-striped table-hover">
            <thead class="thead-default">
            <tr>
                <th>Livro</th>
                <th>Autor</th>
                <th>Ano</th>
                <th>Categoria</th>
                <th>Ativo</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Código Limpo</td>
                <td>Robert Cecil Martin</td>
                <td>2012</td>
                <td>Programação</td>
                <td>Sim</td>
            </tr>
            <tr>
                <td>Refatoração: Aperfeiçoando o Design de Códigos Existentes</td>
                <td>Martin Fowler, Kent Beck</td>
                <td>1999</td>
                <td>Projetos</td>
                <td>Sim</td>
            </tr>
            <tr>
                <td>Design Patterns: Elements of Reusable Object-Oriented</td>
                <td>Erich Gamma</td>
                <td>1994</td>
                <td>Programação</td>
                <td>Sim</td>
            </tr>
            <tr>
                <td>O Programador Apaixonado: Construindo uma carreira </td>
                <td>Chad Fowler</td>
                <td>2014</td>
                <td>Programação</td>
                <td>Sim</td>
            </tr>
            <tr>
                <td>O universo da programação: Um guia de carreira em desenvolvimento de software</td>
                <td>William Oliveira</td>
                <td>2018</td>
                <td>Auto Ajuda</td>
                <td>Sim</td>
            </tr>
        </tbody>
        </table>
        
        
    </body>
</html>
"""

app.run()