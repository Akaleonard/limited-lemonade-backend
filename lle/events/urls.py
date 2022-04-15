from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from events import views

router = routers.DefaultRouter()
router.register('event/', views.EventController.as_view(), basename='event')

# urlpatterns = [
#     path('event/', views.EventController.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
