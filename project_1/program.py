# This program says hello and asks for my name
import sys
import pyperclip

def hello():
    print('Hello World!')
    print('What is your name?')
    myName = input()
    nameLen = len(myName)
    print(f'Great to meet you {myName}')
    print(f'The length of your name is: {nameLen}')
    print('Thanks for using the app! \nExiting')
    sys.exit()

hello()