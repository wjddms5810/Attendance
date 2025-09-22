from user import USER

class Reporter:
    @staticmethod
    def print_points_and_grades(users: list[USER]):
        for user in users:
            print(f"NAME : {user.name}, POINT : {user.get_points()}, GRADE : {user.get_grade()}")

    @staticmethod
    def print_removed_players(users: list[USER]):
        print("\nRemoved player")
        print("==============")
        for user in users:
            if user.get_grade() == "NORMAL" and user.wednesday_count == 0 and user.weekend_count == 0:
                print(user.name)
