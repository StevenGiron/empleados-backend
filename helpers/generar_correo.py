import logging
from flask import jsonify
from models.empleado import Empleado
from utils.db import db

# Metodo para generar correo electronico de acuerdo al primer nombre, primer apellido y pais
def generarCorreo(nombre, apellido, pais):
    try:
        empleados = db.session.query(Empleado).filter_by(primerNombre = nombre, primerApellido = apellido).all()
        
        if len(empleados) < 1:
            n = 0
        else:
            n = len(empleados)
            
        if pais == 'Colombia':
            if n == 0:
                return f'{nombre}.{apellido.replace(" ","")}@stevencorreo.com.co'
            else:
                return f'{nombre}.{apellido.replace(" ","")}.{n}@stevencorreo.com.co'

        if pais == 'Estados Unidos':
            if n == 0:
                return f'{nombre}.{apellido.replace(" ","")}@stevencorreo.com.us'
            else:
                return f'{nombre}.{apellido.replace(" ","")}.{n}@stevencorreo.com.us'

        
    except Exception:
        logging.error('Error al generar correo')
        return jsonify({'msg':'Error al generar correo'})