class Phone: # parent class
    def making_calls(self):
        print("Making calls .. ")
    def attend_calls(self):
        print("Attending calss ... ")
class SmartPhone(Phone): # child class
    def playing_games(self):
        print("Playing high level games")
    def camera(self):
        print("Smartphone has 48 pixels camera")
# creating an object
ss = SmartPhone()
ss.making_calls()
ss.attend_calls()
ss.camera()
ss.playing_games()

# creating object of parent class
pp = Phone()
pp.making_calls()
pp.attend_calls()

