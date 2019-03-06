from django.urls import path
from .views import event, events, add_event, participation

urlpatterns = [
    path('', events, name='events'),
    path('add/', add_event, name='add_event'),
    path('<int:id>/participation/', participation, name='participation'),
    path('<int:id>/', event, name='event'),
]
