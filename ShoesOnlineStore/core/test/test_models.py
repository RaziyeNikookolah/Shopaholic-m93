from django.test import TestCase
from datetime import datetime
from ..models import BaseModel


class BaseModelTest(TestCase):
    def setUp(self):
        self.base_model = BaseModel.objects.create()

    def test_is_deleted_default_value(self):
        self.assertFalse(self.base_model.is_deleted)

    def test_delete(self):
        self.base_model.delete()
        self.assertTrue(self.base_model.is_deleted)
        self.assertIsNotNone(self.base_model.delete_timestamp)

    def test_restore(self):
        self.base_model.delete()
        self.base_model.restore()
        self.assertFalse(self.base_model.is_deleted)
        self.assertIsNotNone(self.base_model.restore_timestamp)

    def test_soft_delete_manager(self):
        self.assertEqual(BaseModel.objects.count(), 1)
        self.assertEqual(BaseModel.deleted_objects.count(), 0)
        self.base_model.delete()
        self.assertEqual(BaseModel.objects.count(), 0)
        self.assertEqual(BaseModel.deleted_objects.count(), 1)

    def test_archive_deleted_manager(self):
        self.assertEqual(BaseModel.objects.count(), 1)
        self.assertEqual(BaseModel.deleted_objects.count(), 0)
        self.base_model.delete()
        self.assertEqual(BaseModel.objects.count(), 0)
        self.assertEqual(BaseModel.deleted_objects.count(), 1)

    def test_restore_deleted(self):
        self.base_model.delete()
        self.base_model.restore()
        self.assertEqual(BaseModel.objects.count(), 1)
        self.assertEqual(BaseModel.deleted_objects.count(), 0)
