# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from pizza import views

router = DefaultRouter()
router.register(r'pizza', views.PizzaModelSerializer, basename='pizza')

urlpatterns = [
    path('', include(router.urls))
]