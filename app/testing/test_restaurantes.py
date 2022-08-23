import unittest

from . import app
from module import gestionar_restaurante 



    

class TestRestaurantes(unittest.TestCase):


    def test_delete(self):
        self.assertTrue(gestionar_restaurante.eliminar_rest(1))
        



if __name__ == '__main__':
    unittest.main()