
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path


from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),

    #path('api/v1/auth/', include('djoser.urls')),
    #path('api/v1/auth-token/', include('djoser.urls.authtoken')),
]


