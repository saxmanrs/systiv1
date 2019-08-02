from django.urls import path, include
from .views import index_urls
from .views import my_logout

urlpatterns = [
path('index/', index_urls, name="index_urls"),
path('logout/', my_logout, name="logout")

]
