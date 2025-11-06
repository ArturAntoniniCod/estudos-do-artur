from flask import Flask,render_template, request, redirect, url_for

app= Flask(__name__)

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
    nome= request.form['nome']
    idade = request.form['idade']
    telefone=request.form['telefone']
    id=request.form['id']
    email=request.form['email']
    RG=request.form['RG']

    alunos.append({'nome':nome,'idade':idade,'telefone':telefone,'id':id,'email':email,'RG':RG})
    return redirect(url_for('index'))
app.run(debug=True)
