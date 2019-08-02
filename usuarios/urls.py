from django.urls import path
from .views import usuarios_list
from .views import usuarios_new
from .views import usuarios_upd
from .views import usuarios_del



urlpatterns = [
path('list/', usuarios_list, name="usuarios_list"),
path('new/', usuarios_new, name="usuarios_new"),
path('upd/<int:id>', usuarios_upd, name="usuarios_upd"),
path('del/<int:id>', usuarios_del, name="usuarios_del"),
]
