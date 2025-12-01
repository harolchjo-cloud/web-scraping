# Ejercicio 20: Testing y Debugging - Código Confiable y Libre de Errores

## ¿Qué es y para qué sirve?
Testing es el proceso de verificar que el código funciona correctamente mediante pruebas automatizadas. Debugging es encontrar y corregir errores. Ambos son esenciales para crear software confiable y mantenible.

## ¿Cómo funciona?
Python incluye `unittest` para crear pruebas automatizadas que verifican el comportamiento esperado del código. Los debuggers permiten ejecutar código paso a paso, inspeccionar variables y encontrar errores.

## Contenido del ejercicio
- `ejercicio20.py`: funciones de ejemplo y pruebas (unitarias, integración y mocking).

## Explicación línea por línea (resumen)
- `import unittest` - Importa framework de testing
- `class TestMiClase(unittest.TestCase):` - Define clase de pruebas
- `def test_funcion(self):` - Define método de prueba
- `self.assertEqual(resultado, esperado)` - Verifica igualdad
- `self.assertTrue(condicion)` - Verifica que sea verdadero
- `self.assertRaises(Exception, funcion)` - Verifica que lance excepción
- `unittest.main()` - Ejecuta todas las pruebas

## Tipos de assertions
- `assertEqual(a, b)`: a == b
- `assertNotEqual(a, b)`: a != b
- `assertTrue(x)`: bool(x) is True
- `assertFalse(x)`: bool(x) is False
- `assertIs(a, b)`: a is b
- `assertIsNone(x)`: x is None
- `assertIn(a, b)`: a in b
- `assertRaises(exc, fun)`: fun() raises exc

## Técnicas de debugging
- `print()` statements
- `pdb` (pdb.set_trace())
- Debbugers en IDE (VSCode, PyCharm)
- `logging` (niveles debug/info/warning/error)
- `assert` statements
- `traceback`

## Funciones especiales útiles
- `pdb.set_trace()` - Punto de interrupción interactivo
- `logging.debug()` - Mensaje de debug configurado con logging
- `traceback.print_exc()` - Imprime excepción completa
- `sys.exc_info()` - Información de excepción actual
- `inspect.stack()` - Información del stack
- `timeit.timeit()` - Medir tiempo de ejecución

## Despliegue local - pasos rápidos
1. No requiere instalación adicional (unittest incluido)
2. Crear/editar `ejercicio20.py` (ya incluido)
3. Ejecutar pruebas:

```bash
python -m unittest ejercicio20.py
```

4. Para coverage:

```bash
pip install coverage
coverage run -m unittest ejercicio20.py
coverage report -m
```

5. Usar debugger:

```bash
python -m pdb ejercicio20.py
```

## Notas sobre mocking
- Usa `unittest.mock.patch` para sustituir funciones externas (como `requests.get`) por objetos controlados en las pruebas.
- Esto permite probar código de integración sin dependencias de red.

## Ejemplo rápido (resumen):

```python
@mock.patch('requests.get')
def test_obtener_y_procesar_ok(self, mock_get):
    mock_resp = MagicMock()
    mock_resp.text = '1, 2, 3.5'
    mock_resp.raise_for_status = lambda: None
    mock_get.return_value = mock_resp

    resultado = obtener_y_procesar('https://ejemplo.local/datos')
    self.assertEqual(resultado, [1.0, 2.0, 3.5])
```

---

## Consejos prácticos
- Escribe pruebas pequeñas y rápidas.
- Mantén las pruebas independientes entre sí.
- Usa CI (GitHub Actions) para ejecutar pruebas automáticamente.
- Mide cobertura pero no la conviertas en único objetivo.

---

¡Listo! El archivo `ejercicio20.py` contiene un sistema de pruebas completo y ejemplificado. Ejecuta las pruebas y dímelo para revisar juntos los resultados.