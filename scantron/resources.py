
from import_export import resources
from scantron.models import Student

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ('std_id', 'name', 'department')
        export_order = ('name', 'std_id', 'department')

def es():
    ds = StudentResource().export()
    print(ds)
    