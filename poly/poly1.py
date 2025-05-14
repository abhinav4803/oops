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
                                                           
# Define class Car
# class Car:
#     def start_engine(self):
#         print("Car engine started.")

# # Define class Bike
# class Bike:
#     def start_engine(self):
#         print("Bike engine started.")

# # Function to start any vehicle
# def start_vehicle(vehicle):
#     vehicle.start_engine()

# # Create instances
# mycar = Car()
# mybike = Bike()

# # Call start_vehicle for both
# start_vehicle(mycar)
# start_vehicle(mybike)
































# Define AudioPlayer class
class AudioPlayer:
    def play(self):
        print("Playing audio")

# Define VideoPlayer class
class VideoPlayer:
    def play(self):
        print("Playing video")


class StreamPlayer:
    def play(self):
        print("Streaming content")


def start_player(player):
    player.play()


audio = AudioPlayer()
video = VideoPlayer()
stream = StreamPlayer()

start_player(audio)
start_player(video)
start_player(stream)

