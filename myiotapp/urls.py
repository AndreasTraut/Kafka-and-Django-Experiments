from django.urls import path
from myiotapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.hello, name="hello"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("mykafkaconsumer", views.mykafkaconsumer, name="mykafkaconsumer"), 
    path("mykafkaproducer", views.mykafkaproducer, name="mykafkaproducer"), 
]