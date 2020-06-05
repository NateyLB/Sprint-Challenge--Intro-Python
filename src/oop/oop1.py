# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.s
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description
    pass

class GroundVehicle(Vehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass

class Car(GroundVehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass

class Motorcycle(GroundVehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass

class FlightVehicle(Vehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass

class Airplane(FlightVehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass

class Starship(FlightVehicle):
    # def __init__(self, name, description):
    #     super().__init__(name, description)
    #     self.name = name
    #     self.name = description
    pass
