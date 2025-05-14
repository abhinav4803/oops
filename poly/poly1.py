# class abhinav:
#   def speak(self):# create class car and bike both having  a mthod start emgint().
#     # create a function stat_vrhicle(vehicle)
#     #that call statr _enginr for any vehicle
#     #use it both car ang bike
#     return "hindii"
# class boss:
#   def speak(self):
#     return "math"
# class adi:
#   def speak(self):
#     return "english"
# def human_lang(person):
#   print(person.speak());

# v=abhinav()
# b=boss()
# a=adi()
# human_lang(v)
# human_lang(b)
# human_lang(a)
# Define class Car
class Car:
    def start_engine(self):
        print("Car engine started.")

# Define class Bike
class Bike:
    def start_engine(self):
        print("Bike engine started.")

# Function to start any vehicle
def start_vehicle(vehicle):
    vehicle.start_engine()

# Create instances
mycar = Car()
mybike = Bike()

# Call start_vehicle for both
start_vehicle(mycar)
start_vehicle(mybike)
