import os

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

reversedNumbers = {
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}


def getFirstInt(line):
    firstIndex = {}
    for num in numbers:
        index = line.find(num)
        if (index < 0): continue
        firstIndex[num] = index
    
    if (len(firstIndex) == 0):
        for char in line:
            if char.isdigit():
                return int(char)
    else:
        first = next(iter(firstIndex))
        for num in firstIndex:
            if firstIndex[num] < firstIndex[first]:
                first = num

        for i in range(min(len(line), firstIndex[first])):
            char = line[i]
            if char.isdigit():
                return int(char)
        return numbers[first]


def getLastInt(rline):
    line = ""
    for char in reversed(rline):
        line += char
    firstIndex = {}
    for num in reversedNumbers:
        index = line.find(num)
        if (index < 0): continue
        firstIndex[num] = index
    
    if (len(firstIndex) == 0):
        for char in line:
            if char.isdigit():
                return int(char)
    else:
        first = next(iter(firstIndex))
        for num in firstIndex:
            if firstIndex[num] < firstIndex[first]:
                first = num

        for i in range(min(len(line), firstIndex[first])):
            char = line[i]
            if char.isdigit():
                return int(char)
        return reversedNumbers[first]


def main():
    file = open(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), 'input.txt'), 'r')
    lines = file.readlines()
    file.close()

    sum = 0
    for line in lines:
        sum += getFirstInt(line) * 10 + getLastInt(line)
        print(sum)

    print(sum)

if __name__ == '__main__':
    main()