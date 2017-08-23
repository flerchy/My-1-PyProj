import re

def MyAnotherFunction():
    Variable = re.compile(r"123")
    print(type(Variable))
    return 0

def OtherFunction(value):
    value *= value
    return value

def Main():
    array = [0, 1, 2, 3, 5, 8]
    for i in array:
        for j in range(1, 5):
            print(i)
            print(OtherFunction(i))
    return 0


if __name__ == "__main__":
    Main()
