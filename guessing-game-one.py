# write a program to guess a user input based on random number 
# guess the number
import random

guessed_number = 0
count = 0

random_number = random.randint(1,9)

while(guessed_number!="exit"):
    guessed_number = int(input("Guess the random number: "))
    count+=1

    if(guessed_number == "exit"):
        break

    if(random_number>guessed_number):
        print("The number guessed by you is lower")
    elif(random_number<guessed_number):
        print("The number guessed by you is higher")
    else:
        print("The number you guessed is right")
        break

    
print("The number of times the user guess: "+str(count))