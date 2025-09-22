class USER:
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
        self._points = 0
        self._grade = ''
        self.wednesday_count = 0
        self.weekend_count = 0

    def add_points(self, points):
        self._points += points

    def get_points(self):
        return self._points

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade

    def add_attendance(self, weekday, points):
        self.attendance[weekday] += 1
        self.add_points(points)
        if weekday == "wednesday":
            self.wednesday_count += 1
        elif weekday in ["saturday", "sunday"]:
            self.weekend_count += 1

    def check_wednesday_and_weekend(self):
        return self.wednesday_count == 0 and self.weekend_count == 0
