from levelupreports.views.users.eventsbyuser import userevents_list
from django.urls import path
from .views import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', userevents_list),
]