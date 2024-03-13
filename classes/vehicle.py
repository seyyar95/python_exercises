#!/usr/bin/python3


class Vehicle:
    def __init__(self, model, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.model = model

    def __str__(self):
        return f"Model: {self.model}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}"