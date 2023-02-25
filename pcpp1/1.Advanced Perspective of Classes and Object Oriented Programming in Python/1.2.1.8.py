"""
    Estimated time
    20 minutes

    Level of difficulty > Easy

    Objectives
        - creating classes, class and instance variables;
        - accessing class and instance variables;

    Scenario
    Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

    A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

    Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

    Your application should keep track of two parameters:
        - the number of apples processed, stored as a class variable;
        - the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

    Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.
"""

from random import uniform
from typing import Dict, Union, List


class Apple:

    def __init__(self) -> None:
        self.weight = uniform(0.2, 0.5)


class Packaging:

    weight_limitation = 300

    @staticmethod
    def packaging(units_needed: int) -> Dict[str, Dict[str, Union[int, List[Apple]]]]:

        truck_packages = {}
        apples_pending = units_needed

        # The packaging process doesn't end until all the apples has been created
        while (apples_pending != 0):

            box = {"total_units": 0, "total_weight": 0, "units": []}

            # Add apples into the box until the weight limit is reached
            while (box.get('total_weight') < Packaging.weight_limitation):
                apple_unit = Apple()

                # Checks if the limit with the created apple has been reach for this box
                if (box.get('total_weight')+apple_unit.weight > Packaging.weight_limitation):
                    break

                # Adds the apple into the box
                box["total_units"] += 1
                box["total_weight"] += apple_unit.weight
                box["units"].append(apple_unit)
                apples_pending -= 1

                # Checks if all the apples need it has been created
                if not apples_pending:
                    break

            # Adds the package into the truck
            truck_packages[f"{len(truck_packages)+1}-BOX"] = box

        return truck_packages


# Ask for apples to the provider
truck = Packaging.packaging(1000)
total_units = total_weight = 0
for label, content in truck.items():
    print(f"Label {label}: Apples {content['total_units']} - Weight {content['total_weight']}")
    total_units += content["total_units"]
    total_weight += content["total_weight"]
print(f"Order: Total Apples {total_units} - Total Weight {total_weight}")
