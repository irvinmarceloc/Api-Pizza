# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from pizza.models import Pizza
from django.contrib.auth.models import User

class IsStandardUser(BasePermission):

    def has_permission(self, request, view):

        try:
            username = User.objects.get(
                is_staff=True
            )
        except User.DoesNotExist:
            return False
        return True