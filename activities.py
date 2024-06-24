userInput = input("What is your name? ")

def sleeping():
    print(userInput, "is sleeping")

def dancing():
    print(userInput, "is dancing")
    

"""
def addTwoNumbers(num1, num2):
    return num1 + num2;

print(addTwoNumbers(577, 656))

"""
sentinel = 0
while True:
    userActivity = int(input("Give us a number: "))
    match userActivity:
        case 1:
            sentinel = 1
            sleeping();
            
        case 2:
            sentinel = 0
            dancing();
    if sentinel:
        exit()
        
    
    

        