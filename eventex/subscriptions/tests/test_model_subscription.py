from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscrtiptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Alexsandro Felix',
            cpf='12345678901',
            email='felix@mail.com',
            phone='5-99999-9999'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_add attr."""
        self.assertIsInstance(self.obj.created_at, datetime)


