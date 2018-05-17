name = "Sofia Medina"

loB= [" I am staring at a wall ", " I am sick of watching Netflix...How is that even possible ", " I am pretending to do Homework "]

print("Hello " + name)

for i in loB:
    if i == " I am staring at a wall":
        print("I am so bored that " + i)
    elif i == " I am sick of watching Netflix...How is that even possible":
        print(" Somehow am I so bored that" + i)
    else:
        print(" I'm supposed to do homework but" + i)


movies = []
while True:
    print("What movie do you like? Type 'end' to quit.")
    answer = input ()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
