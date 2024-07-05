import unittest
from models.base_model import BaseModel
import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.model.id, str)
        self.assertEqual(len(self.model.id), 36)

    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        self.assertEqual(str(self.model), f"[BaseModel] ({self.model.id}) {self.model.__dict__}")

if __name__ == '__main__':
    unittest.main()

