from flask import Flask, render_template, request, redirect, url_for, session
import random
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
app.secret_key = 'clavedeAna'

@app.route('/', methods = ['GET'])    
def get_encuesta():
    return render_template("index.html")


@app.route('/', methods = ['POST'])    
def post_encuesta():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form.get('comment', '')  
    checkbox1 = request.form.get('checkbox1', '') 
    checkbox2 = request.form.get('checkbox2', '') 
    paymentMethod = request.form['paymentMethod']

    session['name'] = name
    session['location'] = location
    session['language'] = language
    session['comment'] = comment
    session['checkbox1'] = checkbox1
    session['checkbox2'] = checkbox2
    session['paymentMethod'] = paymentMethod

    return redirect(url_for('result'))
    
@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    language = session.get('language')
    comment = session.get('comment')
    checkbox1 = session.get('checkbox1')
    checkbox2 = session.get('checkbox2')
    paymentMethod = session.get('paymentMethod')

    return render_template('result.html', name=name, location=location, language=language, comment=comment, checkbox1=checkbox1, checkbox2=checkbox2, paymentMethod=paymentMethod)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

