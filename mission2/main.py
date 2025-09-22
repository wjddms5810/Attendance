from weekday_rule import BaseWeekdayRule
from grade_policy import DefaultGradePolicy
from file_reader import FileReader
from reporter import Reporter
from attendance_service import AttendanceService

FILE_NAME = "attendance_weekday_500.txt"
MAX_FILE_SIZE = 500


def run_attendance_service():
    service = AttendanceService(BaseWeekdayRule(), DefaultGradePolicy())
    reader = FileReader(FILE_NAME, MAX_FILE_SIZE)

    for name, weekday in reader.read():
        service.add_attendance(name, weekday)

    service.process_grades()

    users = service.get_all_users()
    Reporter.print_points_and_grades(users)
    Reporter.print_removed_players(users)

if __name__ == "__main__":
    run_attendance_service()
