from turtle import *

class TurtleGTX(Turtle):
    import random
    rng = random.Random()
    count = 0
    #generate random number btw 1 and 1000 to represent dist @ which tyres flat
    breakdown_dist = rng.randrange(1, 1000)
    
    def jump(self, distance):
        if self.count < self.breakdown_dist:
            self.penup()
            self.forward(distance)
            self.count += abs(distance)
        else:
            return "You have flat tires. Turtle travel limit has been reached"

    def odometer(self):
        print("Distance travelled by turtle is {0}".format(self.count))


    def fix_tyre(self):
        self.count = 0
        
         
        

window = Screen()
window.bgcolor("lightgreen")
tess = TurtleGTX()

