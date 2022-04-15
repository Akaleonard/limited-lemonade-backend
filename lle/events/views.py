from django.http import Http404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class EventsController(ViewSet):
    """
    CRUD for Events 
    """
    def list(self, request, **kwargs):
        return Response({'test': 'success'})
