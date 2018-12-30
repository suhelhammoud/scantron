from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scantron/', include('scantron.urls')),
]

admin.site.site_header = "OMR Scantron Application"
admin.site.site_title = "OMR Scantron Admin Site"
admin.site.index_title= "Welcome to OMR Scantron App"