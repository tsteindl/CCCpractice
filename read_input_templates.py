
def readTokens():
    line = input("Enter input: ")
    tokens = line.split()
    return tokens

def printTokens(*argv):
    for arg in argv:
        print(arg, end="")


def roundAndFormatTo2Digits(f):
    return "{:.2f}".format(round(f, 2))


readTokens()
# code
printTokens()
