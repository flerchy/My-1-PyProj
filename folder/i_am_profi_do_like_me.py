import nltk

def Main():
    a = NewFunc(25)
    print(a)
    IAmSmart()
    return 0

def NewFunc(a):
    a += 15
    return a

def IAmSmart():
    print("that's true!")
    for i in range(0, 10):
        for j in range(-20, 1):
            for k in range(-25, 1):
                print(i, j, k)
                if i == j == k:
                    print("Ура!")
                    return 0

if __name__ == "__main__":
    Main()
