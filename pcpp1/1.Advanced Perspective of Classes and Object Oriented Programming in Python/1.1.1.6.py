"""
    Estimated time > 15-30 minutes

    Level of difficulty > Easy

    Objectives
        - creating classes, methods, and variables;
        - calling methods;
        - getting simple access to instance variables;

    Scenario:
        - create a class representing a mobile phone;
        - your class should implement the following methods:
            - __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
            - turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
            - turn_off() should return the message 'mobile phone is turned off';
            - call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
        - create two objects representing two different mobile phones; assign any random phone numbers to them;
        - implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
        - turn off both mobiles.

    Example output:
        mobile phone 01632-960004 is turned on
        mobile phone 01632-960012 is turned on
        calling 555-34343
        mobile phone is turned off
        mobile phone is turned off
"""


class MobilePhone:

    def __init__(self, number: int) -> None:
        self.number: int = number

    def turn_on(self) -> str:
        return f"mobile phone {self.number} is turned on"

    def turn_off(self) -> str:
        return "mobile phone is turned off"

    def call(self, number: str) -> str:
        return f"calling {number}"


# Example output
mobile_phone_a = MobilePhone('01632-960004')
mobile_phone_b = MobilePhone('01632-960012')
print(mobile_phone_a.turn_on())
print(mobile_phone_b.turn_on())
print(mobile_phone_a.call('555-34343'))
print(mobile_phone_a.turn_off())
print(mobile_phone_b.turn_off())
