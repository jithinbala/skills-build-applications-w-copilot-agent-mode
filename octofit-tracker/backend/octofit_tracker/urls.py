from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, test_user_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('test-users/', test_user_view, name='test-user-view'),
]
