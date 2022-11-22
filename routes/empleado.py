from flask import Blueprint, request, jsonify
import logging

from helpers.generar_correo import generarCorreo
from helpers.validaciones_db import *
from models.empleado import Empleado
from utils.db import db

# Creacion del blueprint para la modularización de la aplicación
empleado_bp = Blueprint('empleado_bp', __name__)

# Endpoint para obtener todos los usuarios de la base de datos
@empleado_bp.route('/',strict_slashes=False)
def obtenerEmpleados():
    try:
        empleados = Empleado.query.all()
        empleadosArr = []

        for empleado in empleados:
            empleado = {
                'id'                  :empleado.id,
                'primerApellido'      :empleado.primerApellido,
                'segundoApellido'     :empleado.segundoApellido,
                'primerNombre'        :empleado.primerNombre,
                'otrosNombres'        :empleado.otrosNombres,
                'paisEmpleo'          :empleado.paisEmpleo,
                'tipoIdentificacion'  :empleado.tipoIdentificacion,
                'numeroIdentificacion':empleado.numeroIdentificacion,
                'correoElectronico'   :empleado.correoElectronico,
                'fechaIngreso'        :empleado.fechaIngreso,
                'area'                :empleado.area,
                'estado'              :empleado.estado,
                'fechaHoraRegistro'   :empleado.fechaHoraRegistro
            }
            empleadosArr.append(empleado)

        logging.info('Petición para obtener empleados realizada correctamente')
        return jsonify(empleadosArr)

    except Exception:
        logging.error(f'La petición para obtener los empleados falló')
        return jsonify({'msg':'Error al obtener empleados'}),400 

# Endpoint para la agregación de nuevos empleados a la base de datos
@empleado_bp.route('/', methods = ['POST'])
def crearEmpleado ():
    try:
        empleado = Empleado(
            primerApellido       = request.json['primerApellido'],
            segundoApellido      = request.json['segundoApellido'],
            primerNombre         = request.json['primerNombre'],
            otrosNombres         = request.json['otrosNombres'],
            paisEmpleo           = request.json['paisEmpleo'],
            tipoIdentificacion   = request.json['tipoIdentificacion'],
            numeroIdentificacion = request.json['numeroIdentificacion'],
            correoElectronico    = generarCorreo(request.json['primerNombre'], 
                                              request.json['primerApellido'],
                                              request.json['paisEmpleo']),
            fechaIngreso         = request.json['fechaIngreso'],
            area                 = request.json['area']
        )

        db.session.add(empleado)
        db.session.commit()
        logging.info(f'Empleado {empleado.primerNombre} registrado correctamente')
        return jsonify({'msg':"empleado registrado",'exito': True}),200

    except Exception as ex:
        logging.error(f'El registro del empleado falló')
        return jsonify({'msg':f'Error al crear el empleado: {str(ex)}'}),400

# Endpoint para actualizar un empleado existente en la base de datos
@empleado_bp.route('/<id>', methods=['GET', 'PUT'], strict_slashes=False)
def actualizarEmpleado(id):
    try:
        empleado = Empleado.query.get(id)
        empleadoExiste(empleado)
             
        if request.method == "PUT":
            (empleado.id,)                   = id,
            (empleado.primerApellido,)       = request.json['primerApellido'],
            (empleado.segundoApellido,)      = request.json['segundoApellido'],
            (empleado.primerNombre,)         = request.json['primerNombre'],
            (empleado.otrosNombres,)         = request.json['otrosNombres'],
            (empleado.paisEmpleo,)           = request.json['paisEmpleo'],
            (empleado.tipoIdentificacion,)   = request.json['tipoIdentificacion'],
            (empleado.numeroIdentificacion,) = request.json['numeroIdentificacion'],
            (empleado.correoElectronico,)    = generarCorreo(request.json['primerNombre'], 
                                                             request.json['primerApellido'], 
                                                             request.json['paisEmpleo']),
            (empleado.fechaIngreso,)         = request.json['fechaIngreso'],
            (empleado.area,)                 = request.json['area'],
            
            db.session.commit()
            logging.info(f'Empleado {empleado.primerNombre} actualizado correctamente')
            return (empleado.serialize)
        else:
            empleado = Empleado.query.get(id)
            logging.info(f'Petición para obtener al empleado {empleado.primerNombre} realizada correctamente')
            return jsonify(empleado.serialize)

    except Exception as ex:
        logging.error(f'Error al actualizar al empleado')
        return jsonify({'msg':f'Error al actualizar empleado: {str(ex)}'}),400

# Endpoint para eliminar un usuario exsitente en la base de datos
@empleado_bp.route('/eliminar/<id>', methods=['GET'],strict_slashes=False)
def eliminarEmpleado(id):
    try:
        empleado = db.session.query(Empleado).filter_by(id=id).first()
        empleadoExiste(empleado)

        db.session.delete(empleado)
        db.session.commit()
        logging.info(f'Empleado {empleado.primerNombre} eliminado correctamente')
        return jsonify({'msg':f'Empleado {empleado.primerNombre} eliminado correctamente'})
        
    except Exception as ex:
        logging.error('Error al eliminar al empleado')
        return jsonify({'msg':f'Error al eliminar empleado: {str(ex)}'}),400