#!/usr/bin/python3
"""
script that starts a Flask web application
"""
# importar la clase Flask q permite generar nuevas instancias de Flask
from flask import Flask
# crear una instancia de Flask, llamada app
app = Flask(__name__)
# strict_slashes permite que cuando una ruta no tenga una barra (/) al final
# la pueda redirigir correctamente
app.strict_slashes = False
# usar un decorador de python, la función route recibe como parámetro la ruta
# en donde queramos que se corra esta función hello


@app.route('/')
# crear una función para imprimir Hello HBNB!
def hello():
    """This function returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Return desired string for /c/<text> route, replace '_' with space
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
