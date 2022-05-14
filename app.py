"""
weight  = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
"""
"""""
secret_number = 9
count = 0
guess_limit =3
while count< guess_limit:
    guess = int(input("Guess: "))
    count += 1
    if guess == secret_number:
        print("You Won.")
        break
else:
    print("Sorry you failed")
"""

command = ""
started  = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started..")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped..")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to stat the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")


