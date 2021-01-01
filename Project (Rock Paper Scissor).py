import random
def gamewin (comp, you):
    if comp==you:
        return None

    elif comp=='r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp=='p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp=='s':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print('computers Turn : Rock(r) Paper(p) Scissor(S)?')
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'P'
elif randNo == 3:
    comp = 's'

you = input('Your Turn: Rock(r) Paper(p) Scissor(s)? ')
a = gamewin(comp, you)

print(f'Computer choose {comp}')
print(f'You choose {you}')

if a == None:
    print('The game is Tie!')
elif a:
    print("You win!")
else:
    print("You Lose!")


