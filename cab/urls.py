from django.urls import path

from . import views

app_name = "cab"
urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'rider/register/', views.register_rider, name='register_rider'),
    path(r'driver/register/', views.register_driver, name='register_driver'),
    path(r'cab/location/update/', views.update_cab_location, name='update_cab_location'),
    path(r'rider/cab/book/', views.book_cab, name='book_cab'),
    path(r'rider/trip/end/', views.end_trip, name='end_trip'),
    path(r'rider/trip/history/update/', views.update_trip_history, name='update_trip_history'),
]
