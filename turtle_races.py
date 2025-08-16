from turtle import Turtle, Screen
import random
screen =Screen()

colors = ["red","yellow","blue","pink", "green","orange"]
turtles =[]
screen.setup(width=500, height=400)
i = 0
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="What is the color of your bet? Available colors: Red, Yellow, Blue, Pink, Green, Orange : ")

while i < len(colors):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.sety(-180)
    tim.goto(-230, tim.ycor() + (i+1)*50)
    turtles.append(tim)
    i = i+1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            result_writer = Turtle()
            result_writer.hideturtle()
            result_writer.penup()
            result_writer.goto(0, 150)  # top of the screen
            result_writer.write(
                f"{'You WON' if winning_color == user_bet else 'You lost'}! "
                f"The winner is {winning_color} turtle!",
                align="center",
                font=("Arial", 16, "bold")
            )
        turtle.forward(random.randint(0,10))
screen.exitonclick()