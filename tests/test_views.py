# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        
    def test_read_one_product(self):
        response = self.client.get("/api/v1/products/1")
        products = response.json
        #tester si code d'etat = 200 si reponse correcte
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(products, dict)
        self.assertEqual(products['name'], "Skello")
        
    def test_read_one_product_not_found(self):
        response = self.client.get("/api/v1/products:id")
        products = response.json
        #tester si code d'etat = 404 si page introuvable
        self.assertEqual(response.status_code, 404)
        self.assertIsNone(products)
    
        
    def test_create(self):
        requete = self.client.post("/api/v1/products:id")
        
    def test_update(self):
        requete = self.client.patch("/api/v1/products:id")
        
    def test_delete(self):
        requete = self.client.delete("api/v1/products:id")
        
        
            