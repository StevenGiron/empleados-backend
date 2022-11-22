from config import DEBUG
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import unittest
import logging

from routes.empleado import empleado_bp

# Cración de la app Flask
app = Flask(__name__)

# Configuración con la base de datos
app.config.from_object('config')

# Configuracion para la ejecucion de los tests
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

# Configuracion de CORS
cors = CORS(app, resources={r"*": {"origins": "*"}})

# Integracióin de SQLAlchemy a la app Flask
SQLAlchemy(app)

# Configuración de loggs
logging.basicConfig(filename='loggs.txt', level=DEBUG)

# Registo del blueprint
app.register_blueprint(empleado_bp, url_prefix = '/empleados')