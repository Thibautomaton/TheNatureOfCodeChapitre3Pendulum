
class Pendulum(object):
    def __init__(self, origin, arm_length, start_angle):
        self.location = PVector(0,0)
        self.origin = origin    
        self.r = arm_length
        self.angle = start_angle
        self.aVelocity = 0.0
        self.aAcceleration = 0.0
        self.damping = 0.995
        
    def go(self):
        self.update()
        self.display()
    
    def update_origin(self, origin):
        self.origin = origin
    
    def update(self):
        gravity = 0.4
        self.aAcceleration = (-1*gravity*sin(self.angle))
        self.aVelocity+=self.aAcceleration
        self.aVelocity*=self.damping
        self.angle +=self.aVelocity
        
        self.location = PVector(self.r*sin(self.angle), self.r*cos(self.angle))
        self.location.add(self.origin)
            
    def display(self):
        stroke(0)
        strokeWeight(5)
        fill(255)
        line(self.origin.x, self.origin.y, self.location.x, self.location.y)
        ellipse(self.location.x, self.location.y, 16, 16)
        
