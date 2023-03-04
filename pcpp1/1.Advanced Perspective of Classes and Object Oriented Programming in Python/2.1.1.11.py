"""
    Estimated time > 10-20 minutes

    Level of difficulty > Medium

    Objectives > improving the student's skills in operating with special methods

    Scenario
        - Extend the class implementation prepared in the previous lab to support the addition and subtraction of
          integers to time interval objects;
        - to add an integer to a time interval object means to add seconds;
        - to subtract an integer from a time interval object means to remove seconds.
"""


from typing import Tuple


class TimeInterval:

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        if not isinstance(hours, int) or not isinstance(minutes, int) or not isinstance(seconds, int):
            raise TypeError('Wrong data type')
        self.total_seconds = seconds + (minutes * 60) + (hours * 3600)

    def __str__(self):
        hours, minutes, seconds = self.__transform_seconds_to_time(self.total_seconds)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('Wrong data type')
        self.total_seconds = self.total_seconds+other

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError('Wrong data type')
        self.total_seconds = self.total_seconds-other

    def __mul__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError('Wrong data type')
        return self.total_seconds*other.total_seconds

    @staticmethod
    def __transform_seconds_to_time(total_seconds: int) -> Tuple[int, int, int]:
        if not isinstance(total_seconds, int):
            raise TypeError('Wrong data type')
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds


# Testing the code
time1 = TimeInterval(hours=1, minutes=50, seconds=1000)
time2 = TimeInterval(hours=2, minutes=50, seconds=1000)

# Changes done
print(time1)
time1+60
print(time1)
print(time2)
time2-60
print(time2)
