# Stepan (Steven) Susorov (UCID: 30197973)

from turtle import Turtle, Screen
import time

class Clock:
    def __init__(self, pen_size, color, time_format, operator, speed):
        self.pen_size = pen_size
        self.color = color
        self.time_format = time_format
        self.operator = operator
        self.speed = speed
    
    def displayClock(self):
        op = self.operator
        
        hour = 0
        op.pensize(self.pen_size)
        op.color(self.color)
        op.speed(self.speed)
        
        for i in range(self.time_format):
            hour += 1
            op.penup()
            op.setheading(-30*i + 60)
            op.forward(150)
            op.pendown()
            op.forward(25)
            op.penup()
            op.forward(25)
            op.write(str(hour), align="center", font=("Times New Roman", 13))
            op.home()
            op.penup()
         
        '''
        op.speed(10)
        
        op.setpos(0, -250)
        op.pensize(self.pen_size//2)
        op.pendown()
        op.circle(250)
        op.penup()
        
        op.setpos(0, (-250 - self.pen_size*2))
        op.pendown()
        op.circle(250 + self.pen_size*2)
        op.penup()
        op.home()
        '''
    
    def displayClockArrows(self):
        arrows = [("red", 130, 60, 2), ("white", 65, 12, 5), ("white", 95, 60, 3)]
        op = self.operator
        
        time_aggregate = time.localtime()
        hour = time_aggregate.tm_hour
        minute = time_aggregate.tm_min
        second = time_aggregate.tm_sec
        
        op.hideturtle()
        
        for arrow in arrows:
            value = None
            op.color(arrow[0])
            if arrows.index(arrow) == 0: value = second
            elif arrows.index(arrow) == 1: value = hour
            else: value = minute
            
            angle = (value/arrow[2])*360
            op.setheading(90)
            op.right(angle)
            op.pensize(arrow[3])
            op.pendown()
            op.forward(arrow[1])
            op.penup()
            op.home()
    
def main():
    screen = Screen()
    screen.setup(500, 500)
    screen.bgcolor("black")
    
    tortoise = Turtle()
    tortoise.shape("turtle")
    tortoise.penup()
    
    clock = Clock(5, "cyan", 12, tortoise, 10)
    clock.displayClock()
    
    screen.tracer(0)
    running = True
    while running:
        clock.displayClock()
        clock.displayClockArrows()
        screen.update()
        tortoise.clear()
        
        time.sleep(1)

if __name__ == '__main__':
    main()