from django.urls import path
from django.conf.urls import include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token

from .views import HelloWorldView, hello_world, login
from .api import SubscriberViewSet

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

urlpatterns = [
    path('jwt-auth', obtain_jwt_token),
    # path('login/', login, name="login"),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('hello_world/', hello_world, name='hello'),
    path("", include(router.urls)),
]
