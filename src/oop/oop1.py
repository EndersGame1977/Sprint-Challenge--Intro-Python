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
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the base class
class Vehicle():
    pass

# Vehicle is the base class to FlightVehicle
class FlightVehicle(Vehicle):
    pass

# FlightVehicle is the base class to Starship
class Starship(FlightVehicle):
    pass

# Vehicle is the base class to GroundVehicle
class GroundVehicle(Vehicle):
    pass

# FlightVehicle is the base class to Airplane
class Airplane(FlightVehicle):
    pass

# GroundVehicle is the base class to Car
class Car(GroundVehicle):
    pass

# GroundVehicle is the base class to Motorcycle
class Motorcycle(GroundVehicle):
    pass
