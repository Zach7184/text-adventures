print("To start, type 'start'")
fromUser = input()
while True:
    if fromUser == "start":
        print("Start game!")
    elif fromUser == "quit": # else if
        print("Game over!")
        break # Ends the while loop
    else:
        print("To start, type 'start'")
    fromUser = input()
