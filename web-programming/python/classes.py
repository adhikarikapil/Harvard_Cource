# Learning how to use classes and about __init__ funtion


# class Point:
#     def __init__(self, x_coordinates, y_coordinates):
#         self.xCoordinate = x_coordinates
#         self.yCoordinate = y_coordinates


# coordinates = Point(4, 3)
# print(f"The X Coordinate of the point is {coordinates.xCoordinate}")
# print(f"The Y Coordinate of the point is {coordinates.yCoordinate}")


# Program for airline to keep track of booking passengers on the flight
class Flight:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True

    def open_seat(self):
        return self.capacity - len(self.passengers)


flight = Flight(5)
passenger = ["Kapil", "Samip", "Robert", "John"]

for name in passenger:
    if flight.add_passenger(name):
        print(f"Successfully boarded {name} in the flight!!!")
    else:
        print(
            f"The boarding failed for {name} due to flight not having enough capacity!!!"
        )
