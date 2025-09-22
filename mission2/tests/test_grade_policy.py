from mission2.grade_policy import DefaultGradePolicy
from mission2.user import USER

import pytest

@pytest.fixture
def user():
    user = USER("TestUser")
    return user

@pytest.fixture
def grade_policy():
    return DefaultGradePolicy()

def test_calculate_bonus_no_bonus(user, grade_policy):
    bonus = grade_policy.calculate_bonus(user)
    assert bonus == 0

def test_calculate_bonus_with_wednesday(user, grade_policy):
    user.attendance["wednesday"] = 10
    bonus = grade_policy.calculate_bonus(user)
    assert bonus == 10

def test_calculate_bonus_with_weekend(user, grade_policy):
    user.attendance["saturday"] = 5
    user.attendance["sunday"] = 5
    bonus = grade_policy.calculate_bonus(user)
    assert bonus == 10

def test_calculate_bonus_with_both(user, grade_policy):
    user.attendance["wednesday"] = 10
    user.attendance["saturday"] = 5
    user.attendance["sunday"] = 5
    bonus = grade_policy.calculate_bonus(user)
    assert bonus == 20

def test_calculate_grade_gold(user, grade_policy):
    user.add_points(50)
    grade = grade_policy.calculate_grade(user)
    assert grade == "GOLD"

def test_calculate_grade_silver(user, grade_policy):
    user.add_points(30)
    grade = grade_policy.calculate_grade(user)
    assert grade == "SILVER"

def test_calculate_grade_normal(user, grade_policy):
    user.add_points(10)
    grade = grade_policy.calculate_grade(user)
    assert grade == "NORMAL"