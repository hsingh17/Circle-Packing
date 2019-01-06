import pygame 
import random
import math

class Circle:
    centers_in_use = []
    circles = []
    MIN_RADIUS = 2
    MAX_RADIUS = 100

    def __init__(self):
        #generate a random center
        self.center = (random.randrange(0,WIDTH), random.randrange(0,HEIGHT))
        
    def grow(self):
        #keep radius growing until collision is true
        for i in range(Circle.MIN_RADIUS, Circle.MAX_RADIUS):
            self.r = i
            if self.check_collision():
                self.r -= 1
                break
                
    def check_collision(self):
        #check if collision between two circles
        this_x, this_y = self.center
        for circle in Circle.circles:
            other_x, other_y = circle.center
            x_distance = this_x - other_x
            y_distance = this_y - other_y
            distance = math.sqrt((x_distance*x_distance) + (y_distance*y_distance))
            if distance <= self.r + circle.r:
                return True
        return False

    def safe(self):
        #check if circle within circle
        this_x, this_y = self.center
        for circle in Circle.circles:
            other_x, other_y = circle.center
            x_distance = this_x - other_x
            y_distance = this_y - other_y
            distance = math.sqrt((x_distance*x_distance) + (y_distance*y_distance))
            if distance <= circle.r:
                return False

        #check if circle within screen
        if this_x + self.r <= WIDTH and this_x - self.r >= 0 and this_y + self.r <= HEIGHT and this_y - self.r >= 0:
            Circle.circles.append(self)
            return True
        else:
            return False


def color():
    return (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

def draw():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        circle = Circle()
        circle.grow()
        x,y = circle.center
        if circle.safe():
            pygame.draw.circle(window, color(), (x,y), circle.r, 1)
        pygame.display.update()


WIDTH =  1080
HEIGHT = 720
FPS = 60
pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Circle Packing")
draw()