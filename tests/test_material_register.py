from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterialRegister(TransactionCase):
    def test_check_buy_price_constraint(self):
        MaterialRegister = self.env['material.reg']
        
        with self.assertRaises(ValidationError):
            MaterialRegister.create({
                'name': 'Test Material',
                'mat_code': 'TEST001',
                'mat_type': 'fabric',
                'buy_price': 50,
                'partner_id': False
            })

        material = MaterialRegister.create({
            'name': 'Test Material 2',
            'mat_code': 'TEST002',
            'mat_type': 'jeans',
            'buy_price': 150,
            'partner_id': False
        })
        self.assertTrue(material)
