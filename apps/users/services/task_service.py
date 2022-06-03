import logging

import requests
from django.conf import settings

from apps.users.const import GEOLOCATION_ABSTRACT_API_URL, HOLIDAY_ABSTRACT_API_URL
from apps.users.models import User


class TaskService:
    @staticmethod
    def task_assign_geolocation(user_id: int, ip: str):
        """
        Get user geolocation based on their IP
        """
        token = settings.ABSTRACTAPI_TOKEN
        params = {
            "api_key": token,
            "ip_address": ip,
        }
        response = requests.get(GEOLOCATION_ABSTRACT_API_URL, params)
        country = response.json()["country"]
        User.objects.filter(id=user_id).update(country=country)

        return country

    @staticmethod
    def task_assign_registered_on_holiday(user_id: int, year: int, month: int, day: int, country: str):
        """
        Assign if user registered on holiday
        """
        token = settings.ABSTRACTAPI_TOKEN
        params = {
            "api_key": token,
            "country": country,
            "year": year,
            "month": month,
            "day": day
        }
        response = requests.get(HOLIDAY_ABSTRACT_API_URL, params)
        user = User.objects.filter(id=user_id)
        if response.json():
            user.update(registered_on_holiday=True)
        else:
            user.update(registered_on_holiday=True)
