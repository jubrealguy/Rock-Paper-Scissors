import random

template = '''Here are the guidelines
Key        Designation
 R             Rock
 P             Paper
 S             Scissors
    '''

tie = """
This is a Tie, play again
* * * * * * * * * * * * * * * """

print("Welcome to the Rock-Paper-Scissors Game")

options = ["R", "P", "S"]
while True:
    print(template)
    player_1 = input("Please, enter a Key: ").upper()
    computer = random.choice(options)

    if player_1 == "P" and computer == "R":
        user = "Paper"
        cpu = "Rock"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("You win")
        break

    elif player_1 == "P" and computer == "S":
        user = "Paper"
        cpu = "Scissors"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("Compter wins")
        break

    elif player_1 == "R" and computer == "P":
        user = "Rock"
        cpu = "Paper"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("Computer wins")
        break

    elif player_1 == "R" and computer == "S":
        user = "Rock"
        cpu = "Scissors"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("You win")
        break

    elif player_1 == "S" and computer == "R":
        user = "Scissors"
        cpu = "Rock"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("Computer wins")
        break

    elif player_1 == "S" and computer == "P":
        user = "Scissors"
        cpu = "Paper"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("Computer wins")
        break

    elif player_1 == "R" and computer == "R":
        user = "Rock"
        cpu = "Rock"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("This is a tie. Play again")
    
    elif player_1 == "P" and computer == "P":
        user = "Paper"
        cpu = "Paper"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("This is a tie. Play again")
    
    elif player_1 == "S" and computer == "S":
        user = "Scissors"
        cpu = "Scissors"
        print("Player ({}) : CPU ({})".format(user, cpu))
        print("This is a tie. Play again")
        
    else:
        print("You chose the wrong Key")

        