"""
    Estimated time > 20 minutes

    Level of difficulty > Easy

    Objectives
        improving the student's skills in operating with multiple inheritance;
        pointing out the nature of multiple inheritance problems.

    Scenario > Your task is to build a multifunction device (MFD) class consisting of methods responsible for document
               scanning, printing, and sending via fax.

    The methods are delivered by the following classes:
        - scan(), delivered by the Scanner class;
        - print(), delivered by the Printer class;
        - send() and print(), delivered by the Fax class.

    Each method should print a message indicating its purpose and origin, like:
        - 'print() method from Printer class'
        - 'send() method from Fax class'

    Work with the created class:
        - create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
        - create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
        - on each object call the methods: scan(), print(), send();
        - observe the output differences. Was the Printer class utilized each time?
"""


class Scanner:
    def scan(self):
        print('scan(), delivered by the Scanner class')


class Printer:
    def print(self):
        print('print(), delivered by the Printer class')


class Fax:
    def send(self):
        print('send(), delivered by the Fax class')

    def print(self):
        print('print(), delivered by the Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


print('MFD_SFP'.center(20, '-'))

obj_1 = MFD_SFP()
obj_1.scan()
obj_1.print()
obj_1.send()

print('MFD_SPF'.center(20, '-'))

obj_2 = MFD_SPF()
obj_2.scan()
obj_2.print()
obj_2.send()
