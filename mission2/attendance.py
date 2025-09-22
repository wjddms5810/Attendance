from user_data import UserData
from weekday_rule import BaseWeekdayRule

FILE_NAME = "attendance_weekday_500.txt"
MAX_FILE_SIZE = 500

BONUS_THRESHOLD = 10
WEEKEND_BONUS = 10
WEDNESDAY_BONUS = 10
SILVER_THRESHOLD = 30
GOLD_THRESHOLD = 50

users = {}
user_count = 0


def add_user_if_not_exists(user_name):
    global user_count

    if user_name not in users:
        user_count += 1
        users[user_name] = UserData(user_name)

    return users[user_name]


def is_weekend(weekday):
    return weekday in ["saturday", "sunday"]


def is_wednesday(weekday):
    return weekday == "wednesday"


def add_user_data(user_name, weekday):
    user_data = add_user_if_not_exists(user_name)
    weekday_rule = BaseWeekdayRule()
    points = weekday_rule.get_weekday_points(weekday)
    user_data.add_attendance(weekday, points)

    if is_wednesday(weekday):
        user_data.wednesday_count += 1
    elif is_weekend(weekday):
        user_data.weekend_count += 1


def calculate_bonus_points(user_data):
    bonus = 0

    if user_data.attendance["wednesday"] >= BONUS_THRESHOLD:
        bonus += WEDNESDAY_BONUS

    weekend_total = user_data.attendance["saturday"] + user_data.attendance["sunday"]
    if weekend_total >= BONUS_THRESHOLD:
        bonus += WEEKEND_BONUS

    return bonus


def calculate_grade(points):
    if points >= GOLD_THRESHOLD:
        return 1
    elif points >= SILVER_THRESHOLD:
        return 2
    else:
        return 0


def process_all_users():
    for user_data in users.values():
        user_data.points += calculate_bonus_points(user_data)
        user_data.grade = calculate_grade(user_data.points)


def get_grade_name(grade_number):
    grade_names = {0: "NORMAL", 1: "GOLD", 2: "SILVER"}
    return grade_names.get(grade_number, "NORMAL")


def print_points_and_grade():
    for user_data in users.values():
        print(f"NAME : {user_data.name}, POINT : {user_data.points}, GRADE : {get_grade_name(user_data.grade)}")


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for user_data in users.values():
        if user_data.grade not in (1, 2) and user_data.wednesday_count == 0 and user_data.weekend_count == 0:
            print(user_data.name)


def read_attendance_file(FILE_NAME):
    try:
        with open(FILE_NAME, encoding='utf-8') as f:
            input = []
            for _ in range(MAX_FILE_SIZE):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    input.append(parts)
            return input
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def input_file():
    input = read_attendance_file(FILE_NAME)
    for parts in input:
        add_user_data(parts[0], parts[1])
    process_all_users()
    print_points_and_grade()
    print_removed_player()


if __name__ == "__main__":
    input_file()
