import unittest
from datetime import datetime
from django.db.models import QuerySet
from django.test import TestCase
from core.models import BaseModel
from shoes.models import Brand


class TestSoftDeleteManager(TestCase):
    def test_soft_delete_manager(self):
        # Create an instance of ConcreteModel
        concrete_model = Brand.objects.create()

        # Check that the object is not deleted initially
        self.assertFalse(concrete_model.is_deleted)

        # Soft delete the object
        concrete_model.delete()

        # Check that the object is marked as deleted and has a delete_timestamp
        self.assertTrue(concrete_model.is_deleted)
        self.assertIsNotNone(concrete_model.delete_timestamp)

        # Check that the restore_timestamp is still None
        self.assertIsNone(concrete_model.restore_timestamp)

        # Restore the object
        concrete_model.restore()

        # Check that the object is not deleted and has a restore_timestamp
        self.assertFalse(concrete_model.is_deleted)
        self.assertIsNotNone(concrete_model.restore_timestamp)


class TestArchiveDeletedManager(TestCase):
    def test_archive_deleted_manager(self):
        # Create a soft-deleted instance of BaseModel
        deleted_model = Brand.objects.create()
        deleted_model.delete()

        # Use the archive deleted manager to get the deleted object
        archived_model = Brand.deleted_objects.get(pk=deleted_model.pk)

        # Check that the retrieved object is deleted
        self.assertTrue(archived_model.is_deleted)


class TestBaseModel(TestCase):
    def test_delete(self):
        # Create an instance of BaseModel
        base_model = Brand.objects.create()

        # Soft delete the object using the custom delete method
        base_model.delete()

        # Check that the object is marked as deleted and has timestamps set
        self.assertTrue(base_model.is_deleted)
        self.assertIsNotNone(base_model.delete_timestamp)

    def test_restore(self):
        # Create a soft-deleted instance of BaseModel
        deleted_model = Brand.objects.create()
        deleted_model.delete()

        # Restore the deleted object using the custom restore method
        deleted_model.restore()

        # Check that the object is not deleted and has timestamps set
        self.assertFalse(deleted_model.is_deleted)
        self.assertIsNotNone(deleted_model.restore_timestamp)


if __name__ == '__main__':
    unittest.main()
