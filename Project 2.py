import random
randNumber = random.randint(1,100)
userguess = None
guesses = 0

while (userguess != randNumber):
    userguess = int(input('Enter your Guess: '))
    guesses +=1
    if(userguess==randNumber):
        print('You guessed it right!')
    else:
        if(userguess>randNumber):
            print('You guessed it wrong! Enter a smaller number')
        else:
            print('You guessed it wrong! Enter a greater number')

print(f'you guessed the number in {guesses} guesses')
input('Thank you, Thats it!')