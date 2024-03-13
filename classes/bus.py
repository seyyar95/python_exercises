#!/usr/bin/python3
from vehicle import Vehicle

class Bus(Vehicle):
    pass


if __name__ == "__main__":
    bus = Bus("School Bus", "180", "12")
    print(bus)
