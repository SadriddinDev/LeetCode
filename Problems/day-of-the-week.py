class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        week_days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

        days = 0

        for y in range(1971, year):
            days += 366 if is_leap(y) else 365

        if is_leap(year):
            month_days[1] = 29

        for m in range(month - 1):
            days += month_days[m]

        days += day - 1

        return week_days[days % 7]

assert Solution().dayOfTheWeek(31, 8, 2019) == "Saturday"
assert Solution().dayOfTheWeek(18, 7, 1999) == "Sunday"
assert Solution().dayOfTheWeek(15, 8, 1993) == "Sunday"