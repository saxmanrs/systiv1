from django.urls import path, include
from .views import index_urls,my_logout,cad_urls



urlpatterns = [
path('index/', index_urls, name="index_urls"),
path('logout/', my_logout, name="logout"),
path('cadastro/', cad_urls, name="cad_urls"),


]
