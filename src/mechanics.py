import time
import math

start_time = time.time()

class Agent: 

    def __init__(self, money, xpos, ypos):
        self.money = money
        self.posx = xpos
        self.posy = ypos
        self.color = "blue"
        self.size = 30
        self.speed = 1

    def move(self, movement, dt):
        self.posx += round(self.speed * movement['x'] / dt)
        self.posy += round( self.speed * movement['y'] / dt)

    def printInfo(self):
        print("----- Timestamp: ",  time.time() - start_time, " -----")
        print("Posx: ", self.posx)
        print("Posy: ", self.posy)
        print("Money: ", self.money)
        print("Speed: ", self.speed)
        print("Color: ", self.color)
        print("Size: ", self.size)



agent1 = Agent(50, 200, 300)
agent1.printInfo()

last_time = time.time()
start_time = time.time()

def update(dt):
    movementx = round(math.cos((time.time()-start_time)*10))
    movementy = round(math.sin((time.time()-start_time)*10))
    agent1.move({'x':movementx, 'y':movementy}, dt)
    print("---- ", time.time()-start_time, " ----")
    print("movements: (", movementx, ", ", movementy, ")")
    agent1.printInfo()

while True:
    current_time = time.time()

    dt = current_time - last_time

    last_time = current_time

    update(dt)

