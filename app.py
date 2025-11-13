from flask import Flask,render_template, request, redirect, url_for
import sqlite3
app= Flask(__name__)
def init_db():
    sql=sqlite3.connect('alunos.db')
    cursor=sql.cursor()
    cursor.execute('''
                   CREATE TABLE alunos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER NOT NULL
                   )
                   
                   
                   ''')
    sql.commit()
    sql.close()
init_db()
alunos=[ {
    'nome':'Gabriel',
    'idade':26,
    'telefone':'11932-1294',
    'id':1,
    'email':'arturantonini@gmail.com',
    'RG':'509.320.321-23'
},
{
    'nome':'Artur',
    'idade':16,
    'telefone':'21932-1294',
    'id':2,
    'email':'Arturantonini@gmail.com',
    'RG':'519.320.321-23'


}]

@app.route('/')
def index():
    return render_template('register.html',pessoa=alunos)

@app.route('/adicionar',methods=['POST'])
def adicionar():
    nome= float(request.form['nome'])
    idade = request.form['idade']
    telefone=request.form['telefone']
    id=request.form['id']
    email=request.form['email']
    RG=request.form['RG']


    sql=sqlite3.connect('alunos.db')
    cursor=sql.cursor()
    cursor.execute('INSERT INTO alunos (nome,idade,telefone,email,RG)VALUES(?,?)',(nome,idade,telefone,id,email,RG))
    sql.commit()
    sql.close()
    return redirect(url_for('register'))

app.run(debug=True)
