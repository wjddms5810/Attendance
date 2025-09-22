from user_data import UserData
from weekday_rule import WeekdayRule
from grade_policy import GradePolicy


class AttendanceService:
    def __init__(self, weekday_rule: WeekdayRule, grade_policy: GradePolicy):
        self.weekday_rule = weekday_rule
        self.grade_policy = grade_policy
        self.users = {}
        self.user_count = 0

    def get_or_create_user(self, name: str) -> UserData:
        if name not in self.users:
            self.user_count += 1
            self.users[name] = UserData(name)
        return self.users[name]

    def add_attendance(self, user_name: str, weekday: str):
        user = self.get_or_create_user(user_name)
        points = self.weekday_rule.get_weekday_points(weekday)
        user.add_attendance(weekday, points)

    def process_grades(self):
        for user in self.users.values():
            user.add_points(self.grade_policy.calculate_bonus(user))
            user.set_grade(self.grade_policy.calculate_grade(user))

    def get_all_users(self):
        return list(self.users.values())

