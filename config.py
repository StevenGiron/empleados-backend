import os

SECRET_KEY = os.urandom(32)

# Habilitar modo DEBUG
DEBUG = True

# URI para la conexion a la base de datos
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/empleados'

# Desactivación de los eventos del sistema y alertas
SQLALCHEMY_TRACK_MODIFICATIONS = False