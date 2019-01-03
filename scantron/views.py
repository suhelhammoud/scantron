from django.shortcuts import render
from django.http import HttpResponse
from .resources import StudentResource

def index(request):
    return render(request, 
    'scantron/index.html', 
    context={"name": "Suhel"})


def export_students(request):
    student_resource = StudentResource()
    dataset = student_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    return response