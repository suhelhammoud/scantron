from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from scantron.models.paper import Paper


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('url', 'name', 'id_number', "num_questions")


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'papers', PaperViewSet)

# for API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('scantron/', include('scantron.urls')),
]

admin.site.site_header = "OMR Scantron Application"
admin.site.site_title = "OMR Scantron Admin Site"
admin.site.index_title = "Welcome to OMR Scantron App"
