#!/usr/bin/python3
"""
unit tests for the functions in base_model.py
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    BaseModel Unittest
    """

    def test_init(self):
        """
        Objects initialization test case
        """
        _model = BaseModel()
        self.assertIsNotNone(_model.id)
        self.assertIsNotNone(_model.created_at)
        self.assertIsNotNone(_model.updated_at)

    def test_save(self):
        """
        Save method test case
        """
        _model = BaseModel()

        prev_updated_at = _model.updated_at

        curr_updated_at = _model.save()

        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict(self):
        """
        To dictionnary method test case
        """
        _mdl = BaseModel()
        _mdl_dict = _mdl.to_dict()
        self.assertIsInstance(_mdl_dict, dict)
        self.assertEqual(_mdl_dict["__class__"], 'BaseModel')
        self.assertEqual(_mdl_dict['id'], _mdl.id)
        self.assertEqual(_mdl_dict['created_at'], _mdl.created_at.isoformat())
        self.assertEqual(_mdl_dict['updated_at'], _mdl.updated_at.isoformat())

    def test_str(self):
        """
        str method test case
        """
        _model = BaseModel()
        self.assertTrue(str(_model).startswith('[BaseModel]'))
        self.assertIn(_model.id, str(_model))
        self.assertIn(str(_model.__dict__), str(_model))


if __name__ == '__main__':
    unittest.main()
