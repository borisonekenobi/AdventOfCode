import os


def getCubeCount(cube: str):
    count = int(cube.strip().split(' ')[0])
    color = cube.strip().split(' ')[1]
    return color, count


def getMinCount(line: str) -> int:
    minRed = 0
    minGreen = 0
    minBlue = 0

    for draw in line:
        cubes = draw.split(',')
        for cube in cubes:
            color, count = getCubeCount(cube)
            if color == 'red' and count > minRed:
                minRed = count
            elif color == 'green' and count > minGreen:
                minGreen = count
            elif color == 'blue' and count > minBlue:
                minBlue = count
    
    return minRed * minGreen * minBlue


def main():
    file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), 'input.txt'), 'r')
    lines = file.readlines()
    file.close()

    sum = 0
    for i in range(len(lines)):
        line = lines[i].split(':')[1].strip().split(';')
        sum += getMinCount(line)

    print(sum)


if __name__ == '__main__':
    main()