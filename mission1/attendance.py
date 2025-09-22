FILE_NAME = "mission1/attendance_weekday_500.txt"
MAX = 500

BONUS_THRESHOLD = 10
WEEKEND_BONUS = 10
WEDNESDAY_BONUS = 10
SILVER_THRESHOLD = 30
GOLD_THRESHOLD = 50

id1 = {}
id_cnt = 0

# dat[사용자ID][요일]
dat = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
wednesday = [0] * 100
weekend = [0] * 100


def add_user_if_not_exists(user_name):
    global id_cnt

    if user_name not in id1:
        id_cnt += 1
        id1[user_name] = id_cnt
        names[id_cnt] = user_name

    return id1[user_name]


def get_weekday_index_and_points(weekday):
    weekday_info = {
        "monday": (0, 1),
        "tuesday": (1, 1),
        "wednesday": (2, 3),
        "thursday": (3, 1),
        "friday": (4, 1),
        "saturday": (5, 2),
        "sunday": (6, 2)
    }
    return weekday_info.get(weekday)


def is_weekend(weekday):
    return weekday in ["saturday", "sunday"]


def is_wednesday(weekday):
    return weekday == "wednesday"


def input2(user_name, weekday):
    user_id = add_user_if_not_exists(user_name)
    index, add_point = get_weekday_index_and_points(weekday)

    if is_wednesday(weekday):
        wednesday[user_id] += 1
    elif is_weekend(weekday):
        weekend[user_id] += 1

    dat[user_id][index] += 1
    points[user_id] += add_point


def read_attendance_file(FILE_NAME):
    try:
        with open(FILE_NAME, encoding='utf-8') as f:
            for _ in range(MAX):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    input2(parts[0], parts[1])
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def calculate_bonus_points(user_id):
    bonus = 0

    if dat[user_id][2] >= BONUS_THRESHOLD:
        bonus += WEDNESDAY_BONUS

    if dat[user_id][5] + dat[user_id][6] >= BONUS_THRESHOLD:
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
    for i in range(1, id_cnt + 1):
        points[i] += calculate_bonus_points(i)
        grade[i] = calculate_grade(points[i])


def get_grade_name(grade_number):
    grade_names = {0: "NORMAL", 1: "GOLD", 2: "SILVER"}
    return grade_names.get(grade_number, "NORMAL")


def print_points_and_grade():
    for i in range(1, id_cnt + 1):
        print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : {get_grade_name(grade[i])}")


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if grade[i] not in (1, 2) and wednesday[i] == 0 and weekend[i] == 0:
            print(names[i])


def input_file():
    read_attendance_file(FILE_NAME)
    process_all_users()
    print_points_and_grade()
    print_removed_player()


if __name__ == "__main__":
    input_file()
