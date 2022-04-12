from curses import meta
from .models import Subscription , metadata
from .serializers import SubscriptionSerializer , metadataSerializer
from rest_framework import generics


class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class metadataList(generics.ListCreateAPIView):
    queryset = metadata.objects.all()
    serializer_class = metadataSerializer

class metadataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = metadata.objects.all()
    serializer_class = metadataSerializer