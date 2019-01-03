from django.contrib import admin
from .resources import StudentResource, PQuestionResource
from import_export.admin import ImportExportModelAdmin

from scantron.models.db_models import Faculty, Department, Student, Module, Teacher
from scantron.models.paper import Paper, PQuestion


def export_paper(modeladmin, request, queryset):
    print("export_paper is called on queryset")
    for obj in queryset:
        qs = PQuestion.objects.filter(paper = obj)
        print(obj)
        for item in qs:
            print(item)

export_paper.short_description = "Export action"

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_filter = ['department',]

@admin.register(PQuestion)
class PQuestionAdmin(ImportExportModelAdmin):
    resource_class = PQuestionResource
    list_filter = ['paper']


class PQuestionInLine(admin.TabularInline):
    model = PQuestion
    extra = 50
    

class PaperAdmin(admin.ModelAdmin):
    model = Paper
    inlines = [PQuestionInLine]
    actions  = [export_paper]

    


admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Teacher)
# admin.site.register(Student)
# admin.site.register(StudentAdmin)
admin.site.register(Module)
# admin.site.register(PQuestionInLine)
admin.site.register(Paper, PaperAdmin)

