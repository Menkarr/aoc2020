import io

def decode(line):
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
    return row, column

def findHighest(inputL):
    high = 0
    for line in inputL:
        row, column = decode(line)
        high = (row * 8 + column) if (row * 8 + column) > high else high
    return high

def main():
    with open("../input.txt") as f:
        inputL = [line.rstrip() for line in f]

    print(findHighest(inputL))

if __name__ == "__main__":
    main()
