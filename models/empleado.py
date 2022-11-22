from utils.db import db
from helpers.validaciones_empleado import *

# Creación del modelo para la instancia de objetos e interacción con la base de datos
class Empleado ( db.Model):
    __tablename__        = 'empleados'
    id                   = db.Column(db.Integer, primary_key = True)
    primerApellido       = db.Column(db.String(20))
    segundoApellido      = db.Column(db.String(20))
    primerNombre         = db.Column(db.String(20))
    otrosNombres         = db.Column(db.String(50))
    paisEmpleo           = db.Column(db.String(20))
    tipoIdentificacion   = db.Column(db.String(20))
    numeroIdentificacion = db.Column(db.String(20))
    correoElectronico    = db.Column(db.String(80))
    fechaIngreso         = db.Column(db.Date)
    area                 = db.Column(db.String(20))
    estado               = db.Column(db.String(10))
    fechaHoraRegistro    = db.Column(db.DateTime)

    def __init__(
        self,
        primerApellido,
        segundoApellido,
        primerNombre,otrosNombres,
        paisEmpleo,
        tipoIdentificacion,
        numeroIdentificacion,
        correoElectronico,
        fechaIngreso,
        area,
        ):

        # Validar tos los campos antes de que sean instanciados
        validarCampoVacio(primerNombre, 'El primer nombre es obligatorio')
        validarLongitud(primerNombre, 20, 'La longitud maxima del primer nombre es de 20 letras')
        validarÑ(primerNombre, 'El primer nombre no puede contener la letra Ñ')
        validarAcentosYLetras(primerNombre, 'El primer nombre solo debe comprender letras entre A-Z y sin acentos')

        validarLongitud(otrosNombres, 50, 'La longitud maxima de otros nombres es de 50 letras')
        validarÑ(otrosNombres, 'otros nombres no puede contener la letra Ñ')
        validarOtrosNombres(otrosNombres, 'Otros nombres solo debe comprender letras entre A-Z, sin acentos ni espacios')

        validarCampoVacio(primerApellido, 'El primer apellido es obligatorio')
        validarLongitud(primerApellido, 20,'La longitud maxima del primer apellido es de 20 letras')
        validarAcentosYLetras(primerApellido, 'El primer apellido solo debe comprender letras entre A-Z y sin acentos')
        validarÑ(primerApellido, 'El primer apellido no puede contener la letra Ñ')

        validarAcentosYLetras(segundoApellido, 'El segundo apellido solo debe comprender letras entre A-Z y sin acentos')
        validarLongitud(segundoApellido, 20, 'La longitud maxima del segundo apellido es de 20 letras')
        validarÑ(segundoApellido, 'El segundo apellido no puede contener la letra Ñ')

        validarCampoVacio(tipoIdentificacion, 'El tipo de identificación es obligatorio')

        validarCampoVacio(numeroIdentificacion, 'El número de identificación es obligatorio')
        validarLongitud(numeroIdentificacion, 20, 'La longitud maxima del número de identificación es de 20 caracteres')
        validarCaracteresIdentificacion(numeroIdentificacion, 'El número de identificación solo puede contener caracteres entre (a-z / A-Z / 0-9 / -)')

        validarCampoVacio(paisEmpleo, 'El país de empleo es obligatorio')
        validarPais(paisEmpleo, 'El pais no puede ser diferente de Colombia o Estados Unidos')

        validarCampoVacio(area, 'El área es obligatoria')

        validarCampoVacio(fechaIngreso, 'La fecha de ingreso es obligatoria')
        validarFechaIngreso(fechaIngreso)

        self.primerApellido       = primerApellido
        self.segundoApellido      = segundoApellido
        self.primerNombre         = primerNombre
        self.otrosNombres         = otrosNombres
        self.paisEmpleo           = paisEmpleo
        self.tipoIdentificacion   = tipoIdentificacion
        self.numeroIdentificacion = numeroIdentificacion
        self.correoElectronico    = correoElectronico
        self.fechaIngreso         = fechaIngreso
        self.area                 = area
        self.estado               = "Activo"
        
    # Searializar el objeto para un mejor manejo    
    @property
    def serialize(self):
        return {
            'id'                  : self.id,
            'primerApellido'      : self.primerApellido,
            'segundoApellido'     : self.segundoApellido,
            'primerNombre'        : self.primerNombre,
            'otrosNombres'        : self.otrosNombres,
            'paisEmpleo'          : self.paisEmpleo,
            'tipoIdentificacion'  : self.tipoIdentificacion,
            'numeroIdentificacion': self.numeroIdentificacion,
            'correoElectronico'   : self.correoElectronico,
            'fechaIngreso'        : self.fechaIngreso,
            'area'                : self.area,
            'estado'              : self.estado,
            'fechaHoraRegistro'   : self.fechaHoraRegistro
        }