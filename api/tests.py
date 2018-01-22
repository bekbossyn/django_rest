from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import BucketList


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucket_list model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucket_list_name = "Write world class code"
        self.bucket_list = BucketList(name=self.bucket_list_name)

    def test_model_can_create_a_bucket_list(self):
        """Test the bucket_list model can create a bucket_list."""
        old_count = BucketList.objects.count()
        self.bucket_list.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucket_list_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucket_list_data,
            format="json")

    def test_api_can_create_a_bucket_list(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
