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
            if user.get_grade() == "NORMAL" and user.check_wednesday_and_weekend():
                print(user.name)
