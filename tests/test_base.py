from app import app
from flask_testing import TestCase
from flask import current_app, url_for
import json

# Tests unitarios
class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    

    def test_app_existe(self):
        self.assertIsNotNone(current_app)


    def test_app_en_modo_test(self):
        self.assertTrue(current_app.config['TESTING'])

    
    def test_empleados_blueprint_exists(self):
        self.assertIn('empleado_bp', self.app.blueprints)


    def test_obtener_empleado_por_id(self):
        response = self.client.get('/empleados/658')

        assert response.status_code == 200


    def test_obtener_empleado_que_no_existe_get(self):
        response = self.client.get('/empleados/0')

        assert response.status_code == 400


    def test_actualizar_empleado_put(self):
        body = {
                "primerNombre"        : "STEVEN", 
                "otrosNombres"        : "JHSDFASDON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ASDF", 
                "tipoIdentificacion"  : "ASDF", 
                "numeroIdentificacion": "5646", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "nueva", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.put('/empleados/658',
            method="PUT",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json["primerNombre"] == body['primerNombre']
        assert response.json["otrosNombres"] == body['otrosNombres']
        assert response.json["primerApellido"] == body['primerApellido']
        assert response.json["segundoApellido"] == body['segundoApellido']
        assert response.json["tipoIdentificacion"] == body['tipoIdentificacion']
        assert response.json["numeroIdentificacion"] == body['numeroIdentificacion']
        assert response.json["paisEmpleo"] == body['paisEmpleo']
        assert response.json["area"] == body['area']


    def test_actualizar_empleado_que_no_existe_put(self):
        body = {
                "primerNombre"        : "STEVEN", 
                "otrosNombres"        : "JHSDFASDON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ASDF", 
                "tipoIdentificacion"  : "ASDF", 
                "numeroIdentificacion": "5646", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "nueva", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.put('/empleados/0',
            method="PUT",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al actualizar empleado: El empleado no existe en la base de datos"



    def test_eliminar_empleado_get(self):
        response = self.client.get('/empleados/eliminar/659')

        assert response.status_code == 200


    def test_eliminar_empleado_que_no_existe(self):
        response = self.client.get('/empleados/eliminar/0')

        assert response.status_code == 400
        assert response.json['msg'] == "Error al eliminar empleado: El empleado no existe en la base de datos"


    def test_obtener_empleados_get(self):
        response = self.client.get(url_for('empleado_bp.obtenerEmpleados'))

        assert response.status_code == 200


    def test_crear_empleado_post(self):
        body = {
                "primerNombre"        : "STEVEN", 
                "otrosNombres"        : "JHSDFASDON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ASDF", 
                "tipoIdentificacion"  : "ASDF", 
                "numeroIdentificacion": "5646", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "nueva", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json['exito'] == True
        assert response.json['msg'] == "empleado registrado"


    def test_crear_empleado_sin_campos_obligatorios(self):
        body = {
            "primerNombre"            : "", 
            "otrosNombres"            : "JHON", 
            "primerApellido"          : "GIRON", 
            "segundoApellido"         : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == 'Error al crear el empleado: El primer nombre es obligatorio'
        

    def test_crear_empleado_con_campos_que_no_permiten_mas_de_20_caracteres(self):
        body = {
                "primerNombre"        : "HHHHHHHHHHHHHHHHHHHHHHHHSSSSSSSSSSSSSSSSSSSSSSSSSSSEEE", 
                "otrosNombres"        : "JHON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: La longitud maxima del primer nombre es de 20 letras"


    def test_crear_empleado_con_Ñ(self):
        body = {
                "primerNombre"        : "Ñ", 
                "otrosNombres"        : "JHON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: El primer nombre no puede contener la letra Ñ"


    def test_crear_empleado_con_primer_nombre_letra_minuscula_y_acento(self):
        body = {
                "primerNombre"        : "n", 
                "otrosNombres"        : "JHON", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: El primer nombre solo debe comprender letras entre A-Z y sin acentos"


    def test_crear_empleado_con_otros_nombres_con_mas_de_50_caracteres(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSDFAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: La longitud maxima de otros nombres es de 50 letras"


    def test_crear_empleado_con_numero_identificacion_con_caracteres_no_permitidos(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456$", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: El número de identificación solo puede contener caracteres entre (a-z / A-Z / 0-9 / -)"


    def test_crear_empleado_con_pais_diferente_a_los_permitidos(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Ecuador", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: El pais no puede ser diferente de Colombia o Estados Unidos"


    def test_crear_empleado_con_pais_diferente_a_los_permitidos(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Ecuador", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: El pais no puede ser diferente de Colombia o Estados Unidos"


    def test_crear_empleado_con_fecha_mayor_a_la_actual(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"                : "2023-10-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: La fecha de ingreso no debe ser superior a la fecha actual"


    def test_crear_empleado_con_fecha_menor_a_un_mes_a_la_actual(self):
        body = {
                "primerNombre"        : "N", 
                "otrosNombres"        : "JHSFF", 
                "primerApellido"      : "GIRON", 
                "segundoApellido"     : "ARCILA", 
                "tipoIdentificacion"  : "Cedula de Ciudadanía", 
                "numeroIdentificacion": "123456", 
                "paisEmpleo"          : "Colombia", 
                "area"                : "Financiera", 
                "fechaIngreso"        : "2022-08-17"
        }
        response = self.client.post(url_for('empleado_bp.crearEmpleado'),
            method="POST",
            data= json.dumps(body),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert response.json['msg'] == "Error al crear el empleado: La fecha de ingreso no puede ser menor a un mes"

