GUESS_VALUE = 10

userGuess = input("Take a guess: ")
#print(type(userGuess))

if userGuess.isdigit():
    #print(type(userGuess))
    if int(userGuess) == GUESS_VALUE:
        print("You guessed correctly")
    else:
        print("Sorry, you guessed wrong")
    
else:
    print("Bad input")