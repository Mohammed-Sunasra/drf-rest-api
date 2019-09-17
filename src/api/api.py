from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from .models import Subscriber
from .serializers import SubscriberModelSerializer


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberModelSerializer
    queryset = Subscriber.objects.all()
    permission_classes = (IsAuthenticated, )