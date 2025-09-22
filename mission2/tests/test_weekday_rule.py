from weekday_rule import BaseWeekdayRule

def test_weekday_rule():
    rule = BaseWeekdayRule()

    assert rule.get_weekday_points('monday') == 1
    assert rule.get_weekday_points('wednesday') == 3
