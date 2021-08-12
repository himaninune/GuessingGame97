import random
n = random.randint(1, 10)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low, guess a number higher than " + str(guess))
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print ("guess is high, guess a number lower than " + str(guess))
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print ("you guessed it!")   
        break
    