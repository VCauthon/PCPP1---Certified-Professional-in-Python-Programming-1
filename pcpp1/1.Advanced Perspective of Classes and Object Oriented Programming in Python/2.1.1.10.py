"""
    Estimated time > 30-60 minutes

    Level of difficulty > Medium

    Objectives > improving the student's skills in operating with special methods
    
    Scenario
        Create a class representing a time interval;
            the class should implement its own method for addition, subtraction on time interval class objects;
            the class should implement its own method for multiplication of time interval class objects by an integer-type value;
            the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
            the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
            check the argument type, and in case of a mismatch, raise a TypeError exception.
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
        if not isinstance(other, TimeInterval):
            raise TypeError('Wrong data type')
        return TimeInterval(*self.__transform_seconds_to_time(self.total_seconds + other.total_seconds))

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError('Wrong data type')
        return TimeInterval(*self.__transform_seconds_to_time(self.total_seconds - other.total_seconds))

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
print(time1+time2)
print(time2-time1)
print(time2*time1)
