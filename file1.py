#import re
#import ast

def MyFirstFunction():
    Variable = NewFunction(15)
    print(Variable)
    return 0

def NewFunction(value):
    value *= value
    return value

def Main():
    for i in range(0, 10):
        for j in range(1, 5):
            MyFirstFunction()
    return 0

if __name__ == "__main__":
    Main()