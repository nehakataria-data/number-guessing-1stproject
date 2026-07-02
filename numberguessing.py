import random 

print("Welcome to number guessing game.\n")

#Secret number
right_number = random.randint(1,5)

print("I've picked a number for you to guess.")
print("The number is between 1 and 5.\n")


#compare
#use an elif statement to make one choice to happen
while True:
    guessed_number = int(input("Enter your guess: "))
    if guessed_number == right_number:
        break

    if guessed_number < 1 or guessed_number > 5:
        print("Invalid guess. Please enter a number between 1 and 5.")

    elif guessed_number > right_number:
        print("Your guess is not correct.")
        print("Give it another shot.")
        print("Choose a lower number.\n")

    else:
        print("Your guess is not correct.")
        print("Give it another shot.")
        print("Choose a higher number.\n")
  

print("\nCorrect guess.")
print("You won. Thank you for playing.")

