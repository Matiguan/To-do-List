from flask import Flask,render_template

app=Flask(__name__)

nombre= 'Edgar'
lista_nombres=['kao','chi','lan','lo']
#ruta
@app.route('/')
#vista
def home():
    return render_template('home.html', nombre=nombre, lista_nombres=lista_nombres)


