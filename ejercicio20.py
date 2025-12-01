"""
Ejercicio 20: Testing y Debugging - Código Confiable y Libre de Errores

Este archivo contiene:
- Funciones ejemplo (suma, división segura, procesamiento simple)
- Una función que simula obtener datos desde la web (usamos requests en producción)
- Pruebas unitarias, integración y uso de mocking con unittest

Cómo ejecutar pruebas:
    python -m unittest ejercicio20.py

Cómo ejecutar con coverage:
    pip install coverage
    coverage run -m unittest ejercicio20.py
    coverage report -m

Cómo depurar con pdb:
    python -m pdb ejercicio20.py

"""

import logging
import requests
import unittest
from unittest import mock
from unittest.mock import MagicMock

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------
# Código bajo prueba
# -----------------------

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def dividir(a, b):
    """Devuelve a / b. Lanza ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("division por cero")
    return a / b


def procesar_datos(raw_list):
    """Recibe una lista de cadenas con números y devuelve lista de floats limpiados.
    Ejemplo: [' 1', '2.5', '3
'] -> [1.0, 2.5, 3.0]
    Si un elemento no es convertible, se ignora.
    """
    resultados = []
    for item in raw_list:
        try:
            texto = item.strip()
            num = float(texto)
            resultados.append(num)
        except Exception:
            # ignorar valores inválidos
            logger.debug("ignorado: %r", item)
    return resultados


def obtener_y_procesar(url):
    """Ejemplo de función de integración que obtiene datos de una URL y los procesa.
    Se espera que la respuesta tenga texto con valores separados por comas.
    """
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    # suponemos que el servidor devuelve: '1, 2.5, 3'
    texto = resp.text
    items = [s for s in texto.split(',')]
    return procesar_datos(items)


# -----------------------
# Pruebas
# -----------------------

class TestFuncionesBasicas(unittest.TestCase):

    def test_sumar_enteros(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(-1, 1), 0)

    def test_sumar_floats(self):
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.30000000000000004)

    def test_dividir_normal(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertAlmostEqual(dividir(1, 3), 0.3333333333333333)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(1, 0)


class TestProcesado(unittest.TestCase):

    def test_procesar_datos_validos(self):
        entrada = ['1', ' 2.5 ', "3\n"]
        salida = procesar_datos(entrada)
        self.assertEqual(salida, [1.0, 2.5, 3.0])

    def test_procesar_datos_invalidos(self):
        entrada = ['a', ' 2', '', '3.1.4']
        salida = procesar_datos(entrada)
        self.assertEqual(salida, [2.0])


class TestIntegracionConMock(unittest.TestCase):
    """
    Aquí demostramos mocking de `requests.get` para pruebas de integración
    sin hacer llamadas reales a la red.
    """

    @mock.patch('requests.get')
    def test_obtener_y_procesar_ok(self, mock_get):
        # Preparar respuesta 'falsa'
        mock_resp = MagicMock()
        mock_resp.text = '1, 2, 3.5'
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp

        resultado = obtener_y_procesar('https://ejemplo.local/datos')
        self.assertEqual(resultado, [1.0, 2.0, 3.5])
        mock_get.assert_called_once()

    @mock.patch('requests.get')
    def test_obtener_y_procesar_http_error(self, mock_get):
        mock_resp = MagicMock()
        def raise_err():
            raise requests.HTTPError('500 Server Error')
        mock_resp.raise_for_status = raise_err
        mock_get.return_value = mock_resp

        with self.assertRaises(requests.HTTPError):
            obtener_y_procesar('https://ejemplo.local/error')


class TestMockingAvanzado(unittest.TestCase):
    @mock.patch('requests.get')
    def test_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout('timeout')
        with self.assertRaises(requests.Timeout):
            obtener_y_procesar('https://ejemplo.local/timeout')


# Ejemplo de uso de logging y punto de debug

def funcion_con_debug(x):
    logger.debug('entrando en funcion_con_debug con %r', x)
    if x < 0:
        # pdb.set_trace()  # descomenta para depuración interactiva
        raise ValueError('x debe ser no negativo')
    return x * 2


class TestDebugging(unittest.TestCase):
    def test_funcion_con_debug_valido(self):
        self.assertEqual(funcion_con_debug(3), 6)

    def test_funcion_con_debug_error(self):
        with self.assertRaises(ValueError):
            funcion_con_debug(-1)


# -----------------------
# Ejecutar pruebas al ejecutar el archivo directamente
# -----------------------

if __name__ == '__main__':
    # Esto permite ejecutar: python -m unittest ejercicio20.py
    unittest.main()
