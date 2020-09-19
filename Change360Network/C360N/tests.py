from django.test import TestCase

from .models import Volunteers


# Create your tests here.
class VolunteersTestCase(TestCase):
    def setUp(self):
        Volunteers.objects.create(
            Full_Name="Aproko Doctor",
            Email_Address="aprokodokita@gmail.com",
            Phone_Number="08012345678",
            Country='NG',
            State="Lagos",
            University="National Open University of Lagos",
        )

    def test_volunteers_details(self):
        doctor = Volunteers.objects.get(Full_Name="Aproko Doctor")
        self.assertEqual(doctor.Email_Address, "aprokodokita@gmail.com")
        self.assertTrue(doctor.Phone_Number, int)
