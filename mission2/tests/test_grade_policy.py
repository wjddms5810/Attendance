from mission2.grade_policy import DefaultGradePolicy
from mission2.user import USER

def test_grade_policy():
    user_data = USER('je.bae')

    user_data.add_attendance('saturday', 2)
    user_data.add_attendance('saturday', 2)
    user_data.add_attendance('sunday', 2)


    grade_policy = DefaultGradePolicy()
    assert grade_policy.calculate_grade(user_data) == 'NORMAL'