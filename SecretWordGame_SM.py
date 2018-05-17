import random

number = random.randint(0,3)

words = ["New York Rangers","LA Kings","New Jersey Devils","Tampa Bay Lightning"]
hint1 = ["NHL hockey team","NHL hockey team","NHL hockey team","NHL hockey team"]
hint2 = ["In the tri-state area","Logo is a crown","Colors are Red, Black and White","In Florida"]
hint3 = ["New York __","LA __","New Jersey __"," Tampa Bay __"]

secretword = words[number]

guess = ""
counter = 1


while True:
    print("Guess the sports team")
    print("Type 'hint1', 'hint2', 'hint3', 'first letter', or 'give up' for answer")
    guess = input ()

    if guess == secretword:
        print("YOU WIN!!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "hint3":
        print( hint3[number] )

    elif guess == "first letter":
        print( secretword[0])

    elif guess == "give up":
        print("pfff. Quiter")
        print("HAHAHAHAHAHHA")
        print("LOSER")
        break

    else:
        print("Guess Again")
        counter += 1
