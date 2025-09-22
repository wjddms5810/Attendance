from abc import ABC, abstractmethod


class WeekdayRule(ABC):
    @abstractmethod
    def get_weekday_points(self, weekday: str):
        pass


class BaseWeekdayRule(WeekdayRule):
    _weekday_points = {
        "monday": 1,
        "tuesday": 1,
        "wednesday": 3,
        "thursday": 1,
        "friday": 1,
        "saturday": 2,
        "sunday": 2
    }

    def get_weekday_points(self, weekday: str):
        return self._weekday_points.get(weekday)
