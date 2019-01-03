
from import_export import resources, fields

from scantron.models.db_models import Student
from scantron.models.paper import PQuestion
from django.contrib import admin
from django.db import models


class PQuestionResource(resources.ModelResource):
    class Meta:
        model = PQuestion
        skip_unchanged = True
        report_skipped = False
        # fields = ( 'paper', 'q_number', 'mark', 'answer')

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = False
        # fields = ('id', 'name')

def es():
    ds = StudentResource().export()
    print(ds)
    