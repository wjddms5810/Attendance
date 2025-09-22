from mission2.attendance_service import AttendanceService
from mission2.weekday_rule import BaseWeekdayRule
from mission2.grade_policy import DefaultGradePolicy
from mission2.file_reader import FileReader
from mission2.reporter import Reporter

FILE_NAME = "attendance_weekday_500.txt"
MAX_FILE_SIZE = 500

def test_attendance_service(capsys):
    service = AttendanceService(BaseWeekdayRule(), DefaultGradePolicy())
    reader = FileReader(FILE_NAME, MAX_FILE_SIZE)

    for name, weekday in reader.read():
        service.add_attendance(name, weekday)

    service.process_grades()

    users = service.get_all_users()
    Reporter.print_points_and_grades(users)
    Reporter.print_removed_players(users)

    out, _ = capsys.readouterr()
    assert out == ('NAME : Umar, POINT : 48, GRADE : SILVER\n'
                   'NAME : Daisy, POINT : 45, GRADE : SILVER\n'
                   'NAME : Alice, POINT : 61, GRADE : GOLD\n'
                   'NAME : Xena, POINT : 91, GRADE : GOLD\n'
                   'NAME : Ian, POINT : 23, GRADE : NORMAL\n'
                   'NAME : Hannah, POINT : 127, GRADE : GOLD\n'
                   'NAME : Ethan, POINT : 44, GRADE : SILVER\n'
                   'NAME : Vera, POINT : 22, GRADE : NORMAL\n'
                   'NAME : Rachel, POINT : 54, GRADE : GOLD\n'
                   'NAME : Charlie, POINT : 58, GRADE : GOLD\n'
                   'NAME : Steve, POINT : 38, GRADE : SILVER\n'
                   'NAME : Nina, POINT : 79, GRADE : GOLD\n'
                   'NAME : Bob, POINT : 8, GRADE : NORMAL\n'
                   'NAME : George, POINT : 42, GRADE : SILVER\n'
                   'NAME : Quinn, POINT : 6, GRADE : NORMAL\n'
                   'NAME : Tina, POINT : 24, GRADE : NORMAL\n'
                   'NAME : Will, POINT : 36, GRADE : SILVER\n'
                   'NAME : Oscar, POINT : 13, GRADE : NORMAL\n'
                   'NAME : Zane, POINT : 1, GRADE : NORMAL\n'
                   '\n'
                   'Removed player\n'
                   '==============\n'
                   'Bob\n'
                   'Zane\n')
