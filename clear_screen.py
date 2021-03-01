from time import sleep
from os import system, name
# print(chr(27) + "[2J")

# define our clear function


def screen_clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# print out some text
# print('Hi !! I am Python\n'*10)
# sleep(2)


# now call function we defined above
screen_clear()
