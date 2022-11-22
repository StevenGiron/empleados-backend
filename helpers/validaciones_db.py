import logging
from types import NoneType

# Validar si el usuario consultado existe en la base de datos
def empleadoExiste(empleado):
    if type(empleado) == NoneType:
        logging.exception('El empleado no existe en la base de datos')
        raise Exception (f'El empleado no existe en la base de datos')