from turtle import Turtle,Screen
import random


is_game_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="This is turtle game",prompt="Bet your wning total color")
color=["red","orange","pink","green","blue","purple"]
y_position=[-100,-60,-20,20,60,100]
all_turtle=[]


if user_bet:
    is_game_on=True


for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(new_turtle)


while is_game_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_on=False
            wining_color=turtle.pencolor()
            if wining_color==user_bet:
                print(f"You have won! the {wining_color} turtle is win")
            else:
                print(f"You have Loss! the {wining_color} turtle is win")

        turtle.forward(random.randint(0,10))



screen.exitonclick()