import logging
import unittest
from app import app


# Puerto en el que se corre la aplicación
PORT = 8080

# Ejecución de la aplicación
if __name__ == '__main__':
    logging.info('Aplicación iniciada')
    logging.info(f'Aplicación corriendo en el puerto {PORT}')
    app.run(debug=True, host="0.0.0.0", port=PORT)