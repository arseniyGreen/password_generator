import os
import random

LETTERS = ['a','b','c','d','e','f','g','h','k','m','n','o','r','s','t','u','x','y','z']
DIGITS = ['0','1','2','3','4','5','6','7','8','9']
SYMBOLS = ['*', '#', '@', '%', "&"]

def genpass():
    password = ''
    for i in range(5):
        password += random.choice(LETTERS)
    password += random.choice(SYMBOLS)
    for i in range(5):
        password += random.choice(DIGITS)

    return password

def main():
    password = genpass()
    try:
        f = open('password.txt', 'w')
    except IOError:
        print('Unable to create file. Check folder access permissions')
        exit()

    f.write(password)
    f.close()

if __name__ == '__main__':
    main()