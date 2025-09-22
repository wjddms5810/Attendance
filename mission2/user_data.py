class UserData:
    def __init__(self, name):
        self.name = name
        self.attendance = {
            "monday": 0,
            "tuesday": 0,
            "wednesday": 0,
            "thursday": 0,
            "friday": 0,
            "saturday": 0,
            "sunday": 0
        }
        self.points = 0
        self.grade = ''
        self.wednesday_count = 0
        self.weekend_count = 0

    def add_points(self, points):
        self.points += points

    def add_attendance(self, weekday, points):
        self.attendance[weekday] += 1
        self.add_points(points)
        if weekday == "wednesday":
            self.wednesday_count += 1
        elif weekday in ["saturday", "sunday"]:
            self.weekend_count += 1

    def set_grade(self, grade):
        self.grade = grade