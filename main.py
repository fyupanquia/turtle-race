# DEPENDENCIAS
from turtle import Turtle, Screen
import random

from sqlalchemy import null
from connection import DataBase

# VARIABLES GLOBALES
is_race_on = False
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [70, 40, 10, -20, -50, -80]
all_turtles = []

# AJUSTES
screen.setup(width=500, height=400)

def Play():
    user_bet = screen.textinput(
            title="Make your bet", 
            prompt="Which turtle will win the race? Enter a color %s: " % "|".join(colors))

    # CREACIÓN DE TORTUGAS
    if len(all_turtles)==0:
        for turtle_index in range(0, 6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.color(colors[turtle_index])
            new_turtle.goto(x=-230, y=y_positions[turtle_index])
            all_turtles.append(new_turtle)
    else:
        for turtle in all_turtles:
            turtle.penup()
            turtle.goto(x=-230, y=y_positions[all_turtles.index(turtle)])


    # INICIAR CARRERA
    if user_bet:
        is_race_on = True

    answer = None
    # BUCLE DEL JUEGO
    while is_race_on:
        for turtle in all_turtles:
            # MOVER CADA TORTUGA HORIZONTALMENTE
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

            # EVALULAR PRIMERA TORTUGA QUE LLEGUE A LA META
            if turtle.xcor() > 230 and is_race_on==True:
                is_race_on = False
                # IDENTIFICACIÓN DE LA TORTUGA GANADORA
                winning_color = turtle.pencolor()
                database = DataBase()
                
                if winning_color == user_bet:
                    database.saveLog(user_bet, winning_color)
                    answer = screen.textinput("You've won!", f'The {winning_color} turtle is the winner!\n Do you want to attempt again? [Y/N]')
                else:
                    database.saveLog(user_bet, winning_color)
                    answer = screen.textinput("You've lost!", f'The {winning_color} turtle is the winner!\n Do you want to attempt again? [Y/N]')
                break

    if answer=="Y":
        Play()
    else:
        Log()


def Log():
    database = DataBase()
    log = database.getLog();
    print("ID\tBET\tWINNER\tDATE")
    for id, bet, winner, date in log:
        print(f"{id}\t{bet}\t{winner}\t{date}")

Play()
screen.exitonclick()