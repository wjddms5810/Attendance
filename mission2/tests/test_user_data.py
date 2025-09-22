from mission2.user_data import UserData

def test_user_data():
    user_data = UserData('je.bae')

    user_data.add_attendance('monday', 1)

    assert user_data.points == 1
    assert user_data.attendance['monday'] == 1


def test_user_data_wednesday():
    user_data = UserData('je.bae')

    user_data.add_attendance('wednesday', 3)

    assert user_data.points == 3
    assert user_data.attendance['wednesday'] == 1


def test_user_data_weekend():
    user_data = UserData('je.bae')

    user_data.add_attendance('saturday', 2)
    user_data.add_attendance('saturday', 2)
    user_data.add_attendance('sunday', 2)

    assert user_data.points == 6
    assert user_data.attendance['saturday'] == 2
    assert user_data.attendance['sunday'] == 1
