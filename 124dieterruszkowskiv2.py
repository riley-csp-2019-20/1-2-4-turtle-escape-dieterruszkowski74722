import turtle as trtl
import random

ike = trtl.Turtle()
ike.pensize(2)
ike.hideturtle()
ike.speed(0)

player = trtl.Turtle()
player.turtlesize(1)
player.setheading(90)
player.pencolor("purple")
player.penup()
player.goto(20, 50)
player.pendown()

line_length = 15 
gap_size = 10 
wall_width = 10 

def draw_door():
  ike.penup()
  ike.forward(gap_size) 
  ike.pendown()

def draw_barrier():
  ike.left(90)
  ike.forward(wall_width) 
  ike.back(wall_width) 
  ike.right(90)

def up():
   player.setheading(90)
   player.forward(10)

def down():
   player.setheading(270)
   player.forward(10)

def left():
   player.setheading(180)
   player.forward(10)

def right():
   player.setheading(0)
   player.forward(10)

for i in range(50):
    print(ike.position())
    if (i > 4):

        door = random.randint(gap_size, line_length-2*gap_size) 
        barrier = random.randint(2*wall_width, line_length-2*gap_size) 
        if (door < barrier):
        
            ike.forward(door)  
            draw_door()
            ike.forward(barrier - door - gap_size) 
            draw_barrier()
            ike.forward(line_length - barrier)
                
        else:
        
            ike.forward(barrier) 
            draw_barrier()
            ike.forward(door - barrier)
            draw_door()
            ike.forward(line_length - door - gap_size)       
    
        ike.left(90) 
    line_length += wall_width



wn = trtl.Screen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.listen()
wn.mainloop()