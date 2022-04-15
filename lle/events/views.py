from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EventController(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        return Response('Get Request')

    def post(self, request, *args, **kwargs):

            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.create(request, *args, **kwargs)