#!/usr/bin/python3
from vehicle import Vehicle

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


if __name__ == "__main__":
    bus = Bus("School Bus", "180", "12")
    print(bus)
    print(bus.seating_capacity())
