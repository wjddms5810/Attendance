from abc import ABC, abstractmethod
from mission2.user_data import UserData

BONUS_THRESHOLD = 10
WEEKEND_BONUS = 10
WEDNESDAY_BONUS = 10
SILVER_THRESHOLD = 30
GOLD_THRESHOLD = 50

class GradePolicy(ABC):
    @abstractmethod
    def calculate_bonus(self, user_data: UserData) -> str:
        pass

    @abstractmethod
    def calculate_grade(self, user_data: UserData) -> str:
        pass



class DefaultGradePolicy(GradePolicy):
    def calculate_bonus(self, user_data: UserData) -> int:
        bonus = 0
        if user_data.attendance["wednesday"] >= BONUS_THRESHOLD:
            bonus += WEDNESDAY_BONUS

        weekend_total = user_data.attendance["saturday"] + user_data.attendance["sunday"]
        if weekend_total >= BONUS_THRESHOLD:
            bonus += WEEKEND_BONUS

        return bonus

    def calculate_grade(self, user_data: UserData) -> str:
        if user_data.points >= GOLD_THRESHOLD:
            return "GOLD"
        elif user_data.points >= SILVER_THRESHOLD:
            return "SILVER"
        return "NORMAL"
