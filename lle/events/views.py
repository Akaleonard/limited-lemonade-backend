from django.http import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from events.models import Events


class EventsController(ViewSet):
    """
    CRUD for Events 
    """
    def list(self, request, **kwargs):
        return Response(Events)

    def post(self, request, format=None):
        return Response({'received data': request.data})

