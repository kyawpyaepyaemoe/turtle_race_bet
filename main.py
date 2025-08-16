from turtle import Turtle, Screen

t =Turtle()
screen =Screen()



def move_forward():
    t.forward(10)

def move_backward():
    t.back(10)

def move_left():
    t.left(10)
def move_right():
    t.right(10)
def clear():
    t.clear()

screen.listen()
screen.onkeypress(key= "w", fun= move_forward)
screen.onkeypress(key= "s", fun= move_backward)
screen.onkeypress(key= "a", fun= move_left)
screen.onkeypress(key= "d", fun= move_right)
screen.onkeypress(key= "c", fun= clear)

screen.exitonclick()