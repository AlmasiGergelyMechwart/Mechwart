import random
from datetime import datetime

class Date():
    def __init__(self, year=1970, month=1, day=1, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def toList(self):
        return (self.year, self.month, self.day, self.hour, self.minute, self.second)
    
    def toInt(self):
        leapDays = (self.year-1969)//4 - (self.year-1901)//100 + (self.year-1601)//400
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        daysFromMonths = 0
        for m in range(1, self.month):
            daysFromMonths += days_in_month[m]
        if self.month > 2 and (self.year%4==0 and self.year%100!=0 and self.year%400==0):
            daysFromMonths+=1
        return ((((self.year-1970)*365 + leapDays + daysFromMonths + self.day-1) * 24 + self.hour) * 60 + self.minute) * 60

    def toIntDatetime(self):
        return int(datetime(*self.toList()).timestamp())
    
    def to_seconds_since_epoch(self):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_days = (self.year - 1969) // 4 - (self.year - 1901) // 100 + (self.year - 1601) // 400

        total_days = (self.year - 1970) * 365 + leap_days
        for m in range(1, self.month):
            total_days += days_in_month[m]
        if self.month > 2 and ((self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0):
            total_days += 1

        total_days += self.day - 1

        total_seconds = total_days * 24 * 60 * 60 + self.hour * 60 * 60 + self.minute * 60 + self.second
        return total_seconds

# time = Date(2024, 4, 17, 8, 10, 30)
# print(time.toIntDatetime())
# print(time.toInt())

for i in range(10):
    time = Date(random.randint(1970, 2024), random.randint(1, 12), random.randint(1, 31), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    print()
    print(time.toIntDatetime())
    # print(time.to_seconds_since_epoch())
    print(time.toInt())