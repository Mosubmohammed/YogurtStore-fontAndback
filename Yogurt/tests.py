from django.test import TestCase
from .models import *

# Create your tests her
class TestUserName(TestCase):
    @classmethod
    def setUpClass(cls):
        Customer.objects.create(First_name='mosab', Last_name='mohammed')
        print(Customer.objects.create(First_name='mosab', Last_name='mohammed'))
        
    def test_first_name_label(self):
        customer=Customer.objects.get(id=1)
        fields_label=customer._meta.get_field('First_name').verbose_name
        self.assertEqual(fields_label,'First name')