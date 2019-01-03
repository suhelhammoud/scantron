from django.contrib import admin

from .models import Faculty, Department, Student, Module, Question, Teacher



# Register models here. TODO remove them after all tests are done

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Module)
admin.site.register(Question)

