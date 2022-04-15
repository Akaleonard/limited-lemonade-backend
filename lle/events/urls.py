from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register('events', views.EventsController, basename='events')
