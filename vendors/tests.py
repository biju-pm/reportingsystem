from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client
from django.utils import timezone
from django.core import mail
from unittest.mock import patch

from .models import Vendor, VendorCategory

User = get_user_model()


class VendorCategoryTestCase(TestCase):
    def setUp(self):
        self.category = VendorCategory.objects.create(name='test category')
        self.category.save()

    def test_vendor_category(self):
        self.assertEqual(self.category.name, 'test category')


# class VendorTestCase(TestCase):
#     def setUp(self):
#         self.category = VendorCategory.objects.create(name='test category')
#         self.category.save()
#         self.vendor = Vendor.objects.create(name='test vendor', category=self.category)
#         self.vendor.save()
#
#     def test_vendor(self):
#         self.assertEqual(self.vendor.name, 'test vendor')
#         self.assertEqual(self.vendor.category.name, 'test category')


class VendorTestCase(TestCase):
    @patch('vendors.models.VendorCategory.objects.create')
    def test_vendor(self, mock_create):
        mock_create.return_value = VendorCategory(name='test category')
        self.category = VendorCategory.objects.create(name='test category')
        self.category.save()
        self.vendor = Vendor.objects.create(name='test vendor', category=self.category)
        self.vendor.save()
        self.assertEqual(self.vendor.name, 'test vendor')
        self.assertEqual(self.vendor.category.name, 'test category')



# mock test example

# from unittest.mock import patch
# from django.test import TestCase
# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model

# from .models import Vendor, VendorCategory

# User = get_user_model()


# class VendorCategoryTestCase(TestCase):
#     def setUp(self):
#         self.category = VendorCategory.objects.create(name='test category')
#         self.category.save()

#     def test_vendor_category(self):
#         self.assertEqual(self.category.name, 'test category')


# class VendorTestCase(TestCase):

#     @patch('vendors.models.VendorCategory.objects.create')
#     def test_vendor(self, mock_create):
#         mock_create.return_value = VendorCategory(name='test category')
#         self.category = VendorCategory.objects.create(name='test category')
#         self.category.save()
#         self.vendor = Vendor.objects.create(name='test vendor', category=self.category)
#         self.vendor.save()
#         self.assertEqual(self.vendor.name, 'test vendor')
#         self.assertEqual(self.vendor.category.name, 'test category')

#         mock_create.assert_called_once_with(name='test category')

