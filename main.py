print("To start, type 'start'")
fromUser = input()
while True:
    if fromUser == "start":
        print("Start game!")
    elif fromUser == "quit": # else if
        print("Game over!")
        break # Ends the while loop
    elif fromUser.split()[0] == "go":
        print("Go somewhere")
    elif fromUser == "attack":
        print("Attack a thing")
    else:
        print("To start, type 'start'")
    fromUser = input()
