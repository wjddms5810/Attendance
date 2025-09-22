import pytest
from mission2.reporter import Reporter
from mission2.user import USER

@pytest.fixture
def users():
    user1 = USER("Alice")
    user1.add_points(50)
    user1.set_grade("GOLD")

    user2 = USER("Bob")
    user2.add_points(30)
    user2.set_grade("SILVER")

    user3 = USER("Charlie")
    user3.add_points(10)
    user3.set_grade("NORMAL")

    return [user1, user2, user3]

def test_print_points_and_grades(users, capsys):
    Reporter.print_points_and_grades(users)
    captured = capsys.readouterr()

    expected_output = (
        "NAME : Alice, POINT : 50, GRADE : GOLD\n"
        "NAME : Bob, POINT : 30, GRADE : SILVER\n"
        "NAME : Charlie, POINT : 10, GRADE : NORMAL\n"
    )
    assert captured.out == expected_output

def test_print_removed_players(users, capsys):
    users[2].check_wednesday_and_weekend = lambda: True

    Reporter.print_removed_players(users)
    captured = capsys.readouterr()

    expected_output = (
        "\nRemoved player\n"
        "==============\n"
        "Charlie\n"
    )
    assert captured.out == expected_output