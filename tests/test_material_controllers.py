from odoo.tests.common import HttpCase
import json

class TestMaterialControllers(HttpCase):
    def test_display_registered_material(self):
        response = self.url_open('/registered-material')
        self.assertEqual(response.status_code, 200)
        material_data = json.loads(response.read())

    def test_display_single_material(self):
        response = self.url_open('/registered-material', params={'_id': 1})
        self.assertEqual(response.status_code, 200)
        material_data = json.loads(response.read())

    def test_update_material(self):
        response = self.url_open('/update-material/1', method='PATCH', json={
            'buy_price': 200
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_material(self):
        response = self.url_open('/delete-material/1', method='DELETE', json={
            'delete': True
        })
        self.assertEqual(response.status_code, 200)
