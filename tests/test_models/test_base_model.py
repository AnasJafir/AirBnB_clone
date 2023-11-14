#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def test_init(self):
        """
        Test for init
        """
        _model = BaseModel()

        self.assertIsNotNone(_model.id)
        self.assertIsNotNone(_model.created_at)
        self.assertIsNotNone(_model.updated_at)

    def test_save(self):
        """
        Test for the save method.
    
        Checks if the save method updates the 'updated_at' attribute.
        """
        _model = BaseModel()

        initial_updated_at = _model.updated_at

        current_updated_at = _model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        To dictionary method test case
        """
        _mdl = BaseModel()
        _mdl_dict = _mdl.to_dict()
        self.assertIsInstance(_mdl_dict, dict)
        self.assertEqual(_mdl_dict["__class__"], 'BaseModel')
        self.assertEqual(_mdl_dict['id'], _mdl.id)
        self.assertEqual(_mdl_dict['created_at'], _mdl.created_at.isoformat())
        self.assertTrue(_mdl_dict['updated_at'].startswith(_mdl.updated_at.isoformat()))

    def test_str(self):
        """
        Test for string representation
        """
        _model = BaseModel()

        self.assertTrue(str(_model).startswith('[BaseModel]'))

        self.assertIn(_model.id, str(_model))

        self.assertIn(str(_model.__dict__), str(_model))


if __name__ == "__main__":
    unittest.main()
