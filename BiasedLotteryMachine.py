import random

def Game():
    print("Rules : You will enter a number b/w 1 and 3 (both included) and if that number is also the number generated by machine, You will win 1000$")
    userInput = int(input("Enter a number b/w 1 and 3 : "))                                             #Taking the input from the user

    while(userInput > 3 or userInput < 1):
        userInput = int(input("Please enter a valid number b/w 1 and 3 (both included) : "))            #Input Validation

    LotteryNumber = random.randint(1,3)                                                                 #Randomly generating the no. to be compared with number entered by the user

    while(userInput == LotteryNumber):                                                                  #Making machine biased
        LotteryNumber = random.randint(1,3)
    
    print(f"The randomly number generated is {LotteryNumber}")
    print("Sorry, use lose the Game.")


if __name__ == '__main__':
    while(True):
        print("\n\n******** Welcome to the lottery Machine ********\n\n")

        Play = int(input("Press 1 to play the Lottery Game and 0 to exit the game : "))                 #Taking input from the user that whether to play the game or not

        while Play <0 or Play >1:                                                                       #Input Validation
            Play = int(input("Please enter a valid number (0 to exit, 1 to play) : "))

        if Play == 1:                                                                                   #User wants to play the game
            Game()
            
        elif Play == 0:                                                                                 #Exit the program
            break


