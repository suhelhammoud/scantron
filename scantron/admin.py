from django.contrib import admin

from .models import Faculty, Department, Student, Module, Question
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Question)