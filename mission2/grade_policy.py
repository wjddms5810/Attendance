from abc import ABC, abstractmethod
from mission2.user import USER

BONUS_THRESHOLD = 10
WEEKEND_BONUS = 10
WEDNESDAY_BONUS = 10
SILVER_THRESHOLD = 30
GOLD_THRESHOLD = 50

class GradePolicy(ABC):
    @abstractmethod
    def calculate_bonus(self, user_data: USER) -> str:
        pass

    @abstractmethod
    def calculate_grade(self, user_data: USER) -> str:
        pass


class DefaultGradePolicy(GradePolicy):
    def calculate_bonus(self, user: USER) -> int:
        bonus = 0
        if user.attendance["wednesday"] >= BONUS_THRESHOLD:
            bonus += WEDNESDAY_BONUS

        weekend_total = user.attendance["saturday"] + user.attendance["sunday"]
        if weekend_total >= BONUS_THRESHOLD:
            bonus += WEEKEND_BONUS

        return bonus

    def calculate_grade(self, user: USER) -> str:
        if user.get_points() >= GOLD_THRESHOLD:
            return "GOLD"
        elif user.get_points() >= SILVER_THRESHOLD:
            return "SILVER"
        return "NORMAL"
