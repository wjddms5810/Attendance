from user_data import UserData

class Reporter:
    @staticmethod
    def print_points_and_grades(user_data: list[UserData]):
        for user in user_data:
            print(f"NAME : {user.name}, POINT : {user.points}, GRADE : {user.grade}")

    @staticmethod
    def print_removed_players(users: list[UserData]):
        print("\nRemoved player")
        print("==============")
        for user in users:
            if user.grade == "NORMAL" and user.wednesday_count == 0 and user.weekend_count == 0:
                print(user.name)
