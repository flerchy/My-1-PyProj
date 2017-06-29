#import math

class vect:
    x = 0
    y = 0

    def Multiply(self, v):
        v2 = vect(0, 0)
        v2.x = v.x * self.x
        v2.y = v.y * self.y
        return v2

    def __init__(self, x: object, y: object) -> object:
        self.x = x
        self.y = y

class dot:
    x = 0
    y = 0

    def Add(self, d):
        d2 = dot(0, 0)
        d2.x = d.x + self.x
        d2.y = d.y + self.y
        return d2

    def __init__(self, x: object, y: object) -> object:
        self.x = x
        self.y = y

def VectorOperations():
    a = vect(2, 4)
    b = vect(5, 2)
    return a.Multiply(b)

def DotOperations():
    a = dot(2, 4)
    b = dot(5, 2)
    return a.Add(b)

def Main():
    res = VectorOperations()
    print(res.x, res.y)
    res = DotOperations()
    print(res.x, res.y)
    return 0

if __name__ == "__main__":
    Main()