from adventure import *

# Constants
START_X = 0
START_Y = 0
MAP_X = 2
MAP_Y = 2

# Variables
rooms = [[0 for j in range(MAP_Y)] for i in range(MAP_X)]
rooms[0][0] = Room("Start")
rooms[0][1] = Room("Forest")
rooms[1][0] = Room("Lake")
rooms[1][1] = Room("End")

x = START_X
y = START_Y

# Commands
def go(direction):
    global x 
    global y 
    if direction == 'north':
        if (y + 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y += 1
    elif direction == 'south':
        if (y - 1) < 0:
            print("There's a wall there")
        else:
            y -= 1
    elif direction == 'west':
        if (x - 1) < 0:
            print("There's a wall there")
        else:
            x -= 1
    elif direction == 'east':
        if (x + 1) >= MAP_X:
            print("There's a wall there")
        else:
            x += 1
    else:
        print("I don't understand which direction you're trying to go")

while True:
    # Print out all the stuff related to the room
    print("At the " + rooms[x][y].name)

    # Get input from the user
    fromUser = input()
    if fromUser == "quit":
        print("Game over!")
        break
    elif fromUser.split()[0] == "go":
        go(fromUser.split()[1])
    else:
        print("That didn't make any sense to me")
