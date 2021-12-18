# Django
from django.conf.urls import url, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import PizzaViewSet

router = DefaultRouter()
router.register("pizza", PizzaViewSet, basename="pizza")

urlpatterns = [
    url('', include(router.urls)),
]