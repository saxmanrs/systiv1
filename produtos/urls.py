from django.urls import path
from .views import produto_list
from .views import produto_new
from .views import produto_upd
from .views import produto_del


urlpatterns = [
    path('list/', produto_list, name="produto_list"),
    path('new/', produto_new, name="produto_new"),
    path('upd/<int:id>', produto_upd, name="produto_upd"),
    path('del/<int:id>', produto_del, name="produto_del"),
]