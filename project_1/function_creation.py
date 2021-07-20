def hello():
    print('Hi! Welcome to my functions')
    user_divide = input('Enter a number to divide by 42!\n')
    while not user_divide.isnumeric():
            user_divide = input('Enter a number (not a string) to divide by 42!\n')
    
    user_divide = int(user_divide)
    try:
        if user_divide:
            print(div42by(user_divide))
            loop = False
    except ValueError:
        print('You did not enter a number')

def div42by(divideby):
    try:
        return 42/ divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

hello()
