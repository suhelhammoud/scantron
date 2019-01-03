from django.test import TestCase
from .resources import StudentResource
from .models import Student


class StudetTest(TestCase):
    def setUp(self):
        Student.objects.create(name="Sami", std_id = "2011300")
        Student.objects.create(name="Ahmad", std_id = "2011500")
        Student.objects.create(name="Omar", std_id = "2011400")

    def test_student_export(self):
        """Student Resource"""
        ds = StudentResource().export()
        print(ds.json)
        print(ds.csv)
        self.assertEqual('Sami' , 'Sami') # TODO