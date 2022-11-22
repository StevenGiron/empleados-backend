import logging
import re
from datetime import timedelta, date

# Validar que el campo para la creación del empleado no pueda estar vacio
def validarCampoVacio(campo, error):
    if campo == "":
        logging.error(f'{error}')
        raise Exception (f'{error}')

# Validar la longitud de los campos para la creación del empleado
def validarLongitud(campo, longitud, error):
    if len(campo) > longitud:
        logging.error(f'{error}')
        raise Exception (f'{error}')

# Validar que los campos no contengan la letra Ñ para la creacion del empleado
def validarÑ (campo, error):
    if re.search('Ñ', campo):
        logging.error(f'{error}')
        raise Exception (f'{error}')

# Validar que el campo solo contenga caracteres entre A-Z
def validarAcentosYLetras(campo, error):
    if campo == "":
        return
    elif (re.match(r'[ A-Z ]+$', campo) is None):
        logging.error(f'{error}')
        raise Exception (f'{error}')

# Validar que el campo otros nombres no contenga espacios y solo caracteres entre la A-Z
def validarOtrosNombres(campo, error):
    if campo == "": 
        return
    elif(re.match(r'[A-Z]+$', campo) is None):
            campo.replace(" ","")
            logging.error(f'{error}')
            raise Exception (f'{error}')

# Validar que el numero de indetificación solo contenga caracteres entre (a-zA-Z0-9-)
def validarCaracteresIdentificacion(campo, error):
    if (re.match(r'[a-zA-Z0-9-]+$', campo) is None):
            logging.error(f'{error}')
            raise Exception (f'{error}')

# Validar que la fecha de ingreso no sea superior a la actual ni inferior a un mes
def validarFechaIngreso(fecha):
    fechaActual = date.today()
    fechaUnMesAtras = fechaActual - timedelta(30)

    if (fecha > str(fechaActual)):
        logging.error('La fecha de ingreso no debe ser superior a la fecha actual')
        raise Exception ('La fecha de ingreso no debe ser superior a la fecha actual')

    if (fecha < str(fechaUnMesAtras)):
        logging.error('La fecha de ingreso no puede ser menor a un mes')
        raise Exception ('La fecha de ingreso no puede ser menor a un mes')

# Validar que el pais de empleo solo sean los definidos
def validarPais(pais, error):
    if (pais != 'Colombia') and (pais != 'Estados Unidos'):
        logging.error(f'{error}')
        raise Exception (f'{error}')