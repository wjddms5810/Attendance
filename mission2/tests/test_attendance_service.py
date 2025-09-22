import os
import pytest
from unittest.mock import MagicMock
from mission2.attendance_service import AttendanceService
from mission2.weekday_rule import WeekdayRule
from mission2.grade_policy import GradePolicy


FILE_NAME = os.path.join(os.path.dirname(__file__), "attendance_weekday_500.txt")
MAX_FILE_SIZE = 500

@pytest.fixture
def attendance_service():
    weekday_rule = MagicMock(spec=WeekdayRule)
    grade_policy = MagicMock(spec=GradePolicy)
    service = AttendanceService(weekday_rule, grade_policy)
    return service, weekday_rule, grade_policy

def test_get_or_create_user(attendance_service):
    service, _, _ = attendance_service

    user = service.get_or_create_user("Alice")
    assert user.name == "Alice"
    assert len(service.users) == 1

    same_user = service.get_or_create_user("Alice")
    assert user == same_user
    assert len(service.users) == 1

def test_add_attendance(attendance_service):
    service, weekday_rule, _ = attendance_service
    weekday_rule.get_weekday_points.return_value = 5

    service.add_attendance("Bob", "monday")
    user = service.get_or_create_user("Bob")

    assert user.attendance["monday"] == 1
    assert user.get_points() == 5

def test_process_grades(attendance_service):
    service, _, grade_policy = attendance_service
    user = service.get_or_create_user("Charlie")
    grade_policy.calculate_bonus.return_value = 10
    grade_policy.calculate_grade.return_value = "Gold"

    service.process_grades()

    assert user.get_points() == 10
    assert user.get_grade() == "Gold"

def test_get_all_users(attendance_service):
    service, _, _ = attendance_service

    service.get_or_create_user("Alice")
    service.get_or_create_user("Bob")

    users = service.get_all_users()
    assert len(users) == 2
    assert users[0].name == "Alice"
    assert users[1].name == "Bob"
