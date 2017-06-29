import re

def my_another_function():
    Variable = re.compile(r"123")
    print(type(Variable))
    return 0


def other_function(value):
    value *= value
    return value


def main():
    array = [0, 1, 2, 3, 5, 8]
    for i in array:
        for j in range(1, 5):
            print(i)
            print(other_function(i))
    return 0


if __name__ == "__main__":
    main()
