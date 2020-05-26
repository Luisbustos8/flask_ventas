import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase): #Hereda de testFlaskBase
    def test_server_is_on(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_route_index_is_lista_regiones(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hola, mundo")



if __name__ == "__main__":
    unittest.main()