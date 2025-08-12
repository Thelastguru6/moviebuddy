from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews.views import UserViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
