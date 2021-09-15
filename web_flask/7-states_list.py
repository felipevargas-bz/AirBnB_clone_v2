#!/usr/bin/python3
"""
script that starts a Flask web application
"""
# importar la clase Flask q permite generar nuevas instancias de Flask
from flask import Flask, render_template
from models import storage
from models.state import State
# crear una instancia de Flask, llamada app
app = Flask(__name__)
# strict_slashes permite que cuando una ruta no tenga una barra (/) al final
# la pueda redirigir correctamente

# usar un decorador de python, la función route recibe como parámetro la ruta
# en donde queramos que se corra esta función hello


@app.route('/states_list', strict_slashes = False)
def list_of_states():
    """
    ...
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown():
    """
    ...
    """
    storage.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
