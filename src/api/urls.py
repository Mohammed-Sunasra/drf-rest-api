from django.urls import path

from .views import HelloWorldView, hello_world


urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('hello_world/', hello_world, name='hello'),
]
