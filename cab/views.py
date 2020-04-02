from django.shortcuts import render

import random
from django.http import JsonResponse
import json
from .models import *
import traceback
import math
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

MAX_COORDINATE = 100


def home(request):
    pass


@csrf_exempt
def get_driver_current_location(driver_id):
    # get driver's current GPS coordinates
    return random.randint(0, MAX_COORDINATE), random.randint(0, MAX_COORDINATE)


@csrf_exempt
def get_rider_current_location(rider_id):
    # get driver's current GPS coordinates
    return random.randint(0, MAX_COORDINATE), random.randint(0, MAX_COORDINATE)


@csrf_exempt
def register_rider(request):
    if "GET" == request.method:
        return render(request, "cab/home.html", {})

    # for POST request
    post_data = request.POST.copy()
    rider_model = RiderModel()
    rider_model.mobile = post_data.get("mobile")
    rider_model.email = post_data.get("email")
    rider_model.name = post_data.get("name")
    rider_model.address = post_data.get("address")
    rider_model.save()

    return JsonResponse({"rider_id": rider_model.user_id})


@csrf_exempt
def register_driver(request):
    if "GET" == request.method:
        return render(request, "cab/home.html", {})

    # for POST request
    post_data = request.POST.copy()
    driver_model = DriverModel()
    driver_model.mobile = post_data.get("mobile")
    driver_model.vehicle_number = post_data.get("vehicle_number")
    driver_model.name = post_data.get("name")
    driver_model.address = post_data.get("address")
    driver_model.save()

    return JsonResponse({"driver_id": driver_model.user_id})


# use this method to update location and availability
@csrf_exempt
def update_cab_location(request):
    post_data = request.POST.copy()
    return _update_cab_location(post_data)


def _update_cab_location(post_data):
    driver_id = post_data.get("driver_id")
    print(post_data)
    x_coordinate = post_data.get("x")
    y_coordinate = post_data.get("y")
    is_available = post_data.get("is_available", True)  # return default TRUE if no value in post data
    location_model = None
    try:
        location_model = LatestLocationModel.objects.get(user_id=driver_id)
    except ObjectDoesNotExist as e:
        location_model = LatestLocationModel()
        location_model.user_id = driver_id
        location_model.x_coordinate = x_coordinate
        location_model.y_coordinate = y_coordinate
        location_model.is_driver_available = is_available
        location_model.save()
        return JsonResponse({"message": "success"})
    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({"message": "bad request"})

    if location_model:
        location_model.user_id = driver_id
        location_model.x_coordinate = x_coordinate
        location_model.y_coordinate = y_coordinate
        location_model.is_driver_available = is_available
        location_model.save()
        return JsonResponse({"message": "success"})

    return JsonResponse({"message": "bad request"})


@csrf_exempt
def book_cab(request):
    post_data = request.POST.copy()
    rider_id = post_data.get("rider_id")
    rider_x = post_data.get("x")
    rider_y = post_data.get("y")

    # get all drivers which are available
    available_drivers = []
    try:
        available_drivers = LatestLocationModel.objects.filter(is_driver_available=True)
    except Exception as e:
        print(traceback.format_exc())

    shortest_distance = max_distance = get_max_distance_possible()
    print("max distance ", max_distance)
    driver = None
    for available_driver in available_drivers:
        driver_x = available_driver.x_coordinate
        driver_y = available_driver.y_coordinate
        d = get_distance_between_rider_and_driver(rider_x, rider_y, driver_x, driver_y)
        if d <= shortest_distance:
            shortest_distance = d
            driver = available_driver

    if shortest_distance == max_distance:
        return JsonResponse({
            "message": "No available driver",
            "driver": 0
        })
    else:
        driver_details = DriverModel.objects.get(user_id=driver.user_id)
        return JsonResponse({
            "message": "Driver available",
            "name": driver_details.name,
            "vehicle_number": driver_details.vehicle_number,
            "mobile": driver_details.mobile,
            "rating": 4.5,
            "distance": shortest_distance,
            "tta": shortest_distance / 50  # lets say average vehicle speed is 50
        })


def get_max_distance_possible():
    # return max distance possible - sqrt( (100-0)^2 + (100- 0)^2)
    return math.sqrt((MAX_COORDINATE - 0) ** 2 + (MAX_COORDINATE - 0) ** 2)


def get_distance_between_rider_and_driver(rider_x, rider_y, driver_x, driver_y):
    rider_x = float(rider_x)
    rider_y = float(rider_y)
    return math.sqrt((rider_x - driver_x) ** 2 + (rider_y - driver_y) ** 2)


@csrf_exempt
def end_trip(request):
    post_data = request.POST.copy()
    driver_id = post_data.get("driver_id")
    x_coordinates = post_data.get("x")
    y_coordinates = post_data.get("y")

    _update_cab_location({"driver_id": driver_id, "x": x_coordinates, "y": y_coordinates})
    _update_trip_history(post_data)
    return JsonResponse({"messages": "success"})


@csrf_exempt
def update_trip_history(request):
    post_data = request.POST.copy()
    _update_trip_history(post_data)
    return JsonResponse({"message": "success"})


def _update_trip_history(post_data):
    driver_id = post_data.get("driver_id")
    rider_id = post_data.get("rider_id")
    x_coordinates = post_data.get("x")
    y_coordinates = post_data.get("y")
    starting_x = post_data.get("start_x")
    starting_y = post_data.get("start_y")

    trip = TripHistoryModel()
    trip.driver_id = driver_id
    trip.rider_id = rider_id
    trip.start_x_coordinate = starting_x
    trip.start_y_coordinate = starting_y
    trip.end_x_coordinate = x_coordinates
    trip.end_y_coordinate = y_coordinates
    trip.save()

    return True
