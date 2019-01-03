from django.contrib import admin
from .resources import StudentResource
from import_export.admin import ImportExportModelAdmin

from scantron.models.db_models import Faculty, Department, Student, Module, Teacher
from scantron.models.paper import Paper, PQuestion



@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


class PQuestionInLine(admin.TabularInline):
    model = PQuestion
    extra = 50


class PaperAdmin(admin.ModelAdmin):
    model = Paper
    inlines = [PQuestionInLine]



admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(StudentAdmin)
admin.site.register(Module)
# admin.site.register(PQuestionInLine)
admin.site.register(Paper, PaperAdmin)

