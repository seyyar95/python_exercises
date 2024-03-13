#!/usr/bin/python3


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def __str__(self):
        return f"Model: {self.name}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}"

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
