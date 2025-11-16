from pendulum import Pendulum

def setup():
    global pendulum1, pendulum2
    size(600, 600)
    pendulum1 = Pendulum(PVector(width/2, 10), 250, PI/4)
    pendulum2 = Pendulum(pendulum1.location, 250, PI/2)
    frameRate(60)

    
def draw():
    background(125)
    global pendulum1, pendulum2
    
    pendulum1.go()
    
    pendulum2.update_origin(pendulum1.location)
    pendulum2.go()
