# Author: Miraj A.
# Description: Builds a game called Pico Centro, a number guessing game that hints users on placement of digits

guess = 10 # Default number of guesses, will be decremented
pica = 0
centro = 0

won = False # User status, boolean deciding whether the user has won or lost
# Three digits
digitOne = 0 # The first digit of the number
digitTwo = 0 # The second digit of the number
digitThree = 0 # The third digit of the number

# User guesses
userDigitOne = -1 # The first digit inputted by the user
userDigitTwo = -1 # The second digit inputted by the user
userDigitThree = -1 # The third digit inputted by the user

def main():
    """Main method that will put the functions and ideas together and will be called at the end of the program"""
    # The start screen, just for decoration
    print("+-----------------------------+")
    print("|   WELCOME TO PICA-CENTRO!   |")
    print("+-----------------------------+")

    # Globalize important variables.
    global guess # Decremented after every instance of the while loop
    global pica 
    global centro # Will be put in an if statement, decides if the user will win
    global won # Boolean value that will cut the loop short if it changes to true

    inputNum() # Allows player to input a number
    clearScreen() # Clears the screen and starts the game

    # While guesses are above 0 AND the answer isn't correct, ask the user for a guess, check it, and draw it
    while guess > 0 and not won:
        print("Guesses left:", guess) # Prints the number of guesses at the top of each round
        userGuess() # Call userGuess
        pica, centro = checkGuess(userDigitOne, userDigitTwo, userDigitThree) # Checks the guess for picas and centros, stores the returned values in the appropriate var
        draw(userDigitOne, userDigitTwo, userDigitThree, pica, centro) # Passes the numbers and values as parameters into the table, which is printed out
        # print(pica, centro) # Just testing

        # If statement checking for victory conditions
        if centro == 3:
            won = True # Changes win condition based on number of centros
            # This will break it out of the while loop and end the game
        guess -= 1 # Decrement guess. If it runs out, then the game is over
    
    # Victory message after going through an if statement
    if won:
        # If the boolean won is true, then this message is displayed
        print("+-------------+")
        print("|   VICTORY   |")
        print("+-------------+")
        print("")
        print("VICTORY! The secret number was: {0}{1}{2}".format(digitOne, digitTwo, digitThree)) # Uses format to insert the correct values
    else:
        # If the boolean won is false, then this message is displayed
        print("+-------------+")
        print("|   DEFEAT!   |")
        print("+-------------+")
        print("")
        print("Better luck next time. The value was {0}{1}{2}".format(digitOne, digitTwo, digitThree)) # Uses format to insert the correct values
        print("")



def clearScreen():
    """Clear screen function to make sure the player doesn't cheat"""
    # Waits for user to press enter, and since python is by default in sequential order, it moves on to clear the screen
    userStart = input("Press enter to start the game!")

    #Adds 100 new lines to 'clear the screen'
    clear = "\n" * 100
    print(clear)


def inputNum():
    """This function will ask a player to input three numbers, and will store the numbers in the appropriate place."""
    # Globalize all variables so it can be called and used throughout the whole program
    global digitOne
    global digitTwo
    global digitThree

    # Ask for user input for first, second, and third digit
    digitOne = eval(input("Please enter the first digit of your number: "))
    digitTwo = eval(input("Please enter the second digit of your number: "))
    digitThree = eval(input("Please enter the third digit of your number: "))

    print("The number is {0}{1}{2}".format(digitOne, digitTwo, digitThree)) # Prints out the number


def userGuess():
    """This method is all about user guessing. The user will pass in their guessing values"""
    # Globalize the needed variables
    global userDigitOne
    global userDigitTwo
    global userDigitThree

    # Take in user input for each slot and stores it into three variables. Each variable will be constantly updated throughout the game
    userDigitOne = eval(input("Please enter your first guess: "))
    userDigitTwo = eval(input("Please enter your second guess: "))
    userDigitThree = eval(input("Please enter your third guess: "))



def checkGuess(guess1, guess2, guess3):
    """This function will check the guess and make sure everything is in the correct place. """

    global pica
    global centro

    # Reset pica and centro to 0 for every time being checked
    # This way, we don't accidentally add one to the previous values of pica and centro, which would cause great confusion
    # Since it is reset, it will check the answers correctly
    pica = 0
    centro = 0

    # The guesses are inputted as parameters, and are put into if statements       


    if guess1 == digitOne:
        centro += 1     # If the guess is in the correct spot, then one is added to centro.
    else:
        # However, if centro is not true, then the value given is put through an inner if statement
        # That will determine if the program needs to add a value to the pica variable
        if guess1 == digitTwo or guess1 == digitThree:    
         # If the guess is equalto another digit, one is added to pica
            pica += 1

    # Repeat if statement for guess 2
    if guess2 == digitTwo:
        centro += 1
    else:
        if guess2 == digitOne or guess2 == digitThree:
            pica += 1
    
    # Repeat if statement for guess 3
    if guess3 == digitThree:
        centro += 1
    else:
        if guess3 == digitOne or guess3 == digitTwo:
            pica += 1
    return pica, centro

def draw(guess1, guess2, guess3, pica, centro):
    """Draws the table to make the game look more appealing.
    Takes in paramaters: user guesses, pica, centro.
    These parameters will be formatted into strings that will be printed together"""

    # The row that splits sections
    splRow = "+--------------------+----------+-------------+"

    # Label row
    mLabel = "|     Your Guess     |   Pica   |    Centro   |"

    # The actual data
    numLab = "|        {one}{two}{three}         |    {p}     |      {c}      |".format(one = guess1, two = guess2, three = guess3, p = pica, c = centro)
    # The above string Uses .format() to insert the different values, useful since they are constantly being updated

    # Print the table in the correct order
    print(splRow)
    print(mLabel)
    print(splRow)
    print(numLab)
    print(splRow)



main()