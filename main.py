# TURTLE RACING GAME
# FASTEST TURTLE WINS, FIRST TO REACH THE FINISH LINE IS THE WINNER!
# TURTLES ARE DEFINED BY THEIR COLOR IN THIS PROGRAM

import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

balance = 50

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a number...")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a number between 2 - 10 ...")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def controlled_turtle():
    pass

# 'colors' define the turtle individuals, basically number of colors define howmany turtles will be racing
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


#Initialize the Turtle Race Screen
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
print(f"{racers} number of turtles will be racing ...")

init_turtle()

def get_bet():
    global balance

    print(f"Your balance is {balance}$")
    if balance <= 0:
        print("Sorry, your balance is not sufficient. Can not bet ...")
    else:
        while True:
            betAmount = input("Enter the amount you want to bet: ")
            if betAmount.isdigit():
                betAmount = float(betAmount)
            else:
                print("Enter a sufficient number...")
                continue
            
            if betAmount <= balance:
                balance = balance - betAmount
                return betAmount
            else:
                print("Insufficient balance...")
                continue

def bet_calculation(betAmount, winner, users_turtle):
    
    global balance

    if users_turtle == winner:
        print("You Won !!!")
        balance = (betAmount * 2) + balance
        print(f"Your balance went up to {balance}$")
    else:
        print("Unfortunately your turtle lost ...")
        
    




random.shuffle(COLORS)
colors = COLORS[:racers] # slice up to 'racers' amount of racers    Ex: [1,2,3,4] [:2] => [1,2]

formatted_colors = " - ".join(colors)

while True:
    users_turtle = input(f"{formatted_colors} colored turtles will be racing, bet on one: ").lower()

    if users_turtle not in colors:
        print("Invalid turtle...")
        continue
    else:
        index = colors.index(users_turtle)
        break


bet_amount = get_bet()


winner = race(colors)

bet_calculation(bet_amount, winner, users_turtle)

print(f"Winner turtle is the {winner} turtle")