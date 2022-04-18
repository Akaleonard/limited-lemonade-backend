from .models import Events
from rest_framework_mongoengine.serializers import DocumentSerializer

class EventsSerializer(DocumentSerializer):
    class Meta:
        model = Events
        depth = 2
