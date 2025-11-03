from flask import Flask,render_template, request, redirect, url_for

app= Flask(__name__)

aluno={
    'nome':'Gabriel',
    'idade':26,
    'telefone':'11932-1294'
}

@app.route('/')
def teste():
    return render_template('index.html',pessoa=aluno)

app.run(debug=True)













