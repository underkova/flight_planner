

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ), #обратились к views и названию метода в этом файле
    path('planning', views.planning ),
    path('instructor_flight_time', views.instructor_flight_time)
    ]