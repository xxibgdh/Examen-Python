import unittest
from libro import Libro
from autor import Autor
from examen import mas_antiguos

class Pruebas(unittest.TestCase):

    def test_mas_antiguos(self):
        libros = [Libro(1, "Lazarillo", 1352), Libro(2, "Quijote", 1462), Libro(3, "Hola", 2000)]
        self.assertEqual(mas_antiguos(libros, 1992), ['Lazarillo', 'Quijote'])
        self.assertRaisesRegex(ValueError, "El año no es válido.", mas_antiguos, libros, 1500)
        self.assertRaisesRegex(ValueError, "El año no es válido.", mas_antiguos, libros, 2022)

if __name__ == "__main__":
    unittest.main()