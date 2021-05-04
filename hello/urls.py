from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.hello, name="hello"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("mykafkaview", views.mykafkaview, name="mykafkaview"), 
]