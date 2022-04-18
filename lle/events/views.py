import pdb
from django.http import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from events.models import Events
from .serializers import EventsSerializer

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass


class EventsController(ViewSet):
    """
    CRUD for Events 
    """
    def list(self, request, **kwargs):
        events = Events.objects()
        serializer = EventsSerializer(events, many=True)
        # pdb.set_trace()
        return Response(serializer.data)

    # def get(self, request, **kwargs):
    #     events = Events.objects()
    #     serializer = EventsSerializer(events)
    #     # pdb.set_trace()
    #     return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = EventsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

