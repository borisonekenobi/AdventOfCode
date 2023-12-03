import os


# Checks that the count of each of the cubes is valid
def checkCube(cube: str) -> bool:
    count = int(cube.strip().split(' ')[0])
    color = cube.strip().split(' ')[1]
    if color == 'red' and count > 12:
        return False
    elif color == 'green' and count > 13:
        return False
    elif color == 'blue' and count > 14:
        return False
    else:
        return True


# Checks that each of the cubes in the draw are valid
def checkDraw(draw: str) -> bool:
    cubes = draw.split(',')
    for cube in cubes:
        if not checkCube(cube):
            return False
    
    return True


# Checks that each of the draw is valid
def checkLine(line: str) -> bool:
    for draw in line:
        if not checkDraw(draw):
            return False
    
    return True


def main():
    file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), 'input.txt'), 'r')
    lines = file.readlines()
    file.close()

    sum = 0
    for i in range(len(lines)):
        line = lines[i].split(':')[1].strip().split(';')
        if checkLine(line):
            sum += i + 1

    print(sum)


if __name__ == '__main__':
    main()