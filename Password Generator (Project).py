# need to import string and random module 
import string
import random

# for lowercase letters 
s1 = string.ascii_lowercase

# for uppercase letters 
s2 = string.ascii_uppercase

# for digits
s3 = string.digits

# for puncutations 
s4 = string.punctuation

# asking user for the length of the password they want to set
plen = int(input('Enter the lenght of the Password: '))

# all the above characters will be generated in the below variable
s=[]

# extend is used to collet all the characters in one variable
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# by printing we can know how it looks
# print(s)

# to randomize the characters
# random.shuffle(s)
# print(''.join(s[0:plen]))

# alternate method to generate password
print('Your Password is: ')
print(''.join(random.sample(s, plen)))