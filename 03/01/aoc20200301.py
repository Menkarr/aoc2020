import io

def parse(mapT):
    line, column, acc = 0, 0, 0
    while line < len(mapT):
        print(mapT[line][column])
        acc += 1 if mapT[line][column] == '#' else 0
        column += 3 - len(mapT[line]) if (column + 3 >= len(mapT[line])) else 3
        line += 1
    return acc

def main():
    with open("../input.txt") as f:
        inputL = [line.rstrip() for line in f]

    print(parse(inputL))

if __name__ == "__main__":
    main()
