import unittest

class Reserva():
    
    # Clase reserva de prueba
    
    def __init__(self, data):
        data = data

class Test_reserva(unittest.TestCase):

    def test_reserva_exitosa(self):
        
        new_reserva = Reserva(0)
        
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
