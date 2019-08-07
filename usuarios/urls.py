from django.urls import path
from .views import ativos_list
from .views import ativos_new
from .views import ativos_upd
from .views import ativos_del



urlpatterns = [
path('list/', ativos_list, name="ativos_list"),
path('new/', ativos_new, name="ativos_new"),
path('upd/<int:id>', ativos_upd, name="ativos_upd"),
path('del/<int:id>', ativos_del, name="ativos_del"),
]
