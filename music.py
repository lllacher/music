class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bang", "Tap", "Boom"])

    def count(self):
        print("One Two Three Four")

    def combust(self):
        print("Going wild - not entirely sure what this is.")

class Band(object):
    def __init__(self, musicians):
        # Call the __init__ method of the parent class
        self.musicians = musicians

    def hire(self, musician):
        self.musicians.append(musician)

    def fire(self, musician):
         self.musicians.remove(musician)
