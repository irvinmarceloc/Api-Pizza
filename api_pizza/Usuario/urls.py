
from django.conf.urls  import url
from .views import UsuarioList

urlpatterns = [
    url(r'^usuario/', UsuarioList.as_view(), name='usuario_list'),
]