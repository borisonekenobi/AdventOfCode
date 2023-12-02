import os

def getFirstInt(line):
    for char in line:
        if char.isdigit():
            return int(char)


def getLastInt(line):
    for char in reversed(line):
        if char.isdigit():
            return int(char)


def main():
    file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), 'input.txt'), 'r')
    lines = file.readlines()
    file.close()

    sum = 0
    for line in lines:
        sum += getFirstInt(line) * 10 + getLastInt(line)

    print(sum)

if __name__ == '__main__':
    main()