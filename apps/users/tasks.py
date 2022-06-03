import dramatiq
import logging

from apps.users.services.task_service import TaskService


@dramatiq.actor
def set_user_country_and_registered_on_holiday(user_id: int, ip: str, year: int, month: int, day: int):
    logging.info("Setting user country and registered on holiday value")
    country = TaskService.task_assign_geolocation(user_id, ip)
    if country is None:
        # It would fire on local machine cause localhost ip returns None value
        raise Exception("Wrong country")
    TaskService.task_assign_registered_on_holiday(user_id, year, month, day, country)
