import io

def parse(mapT, right, down):
    line, column, acc = 0, 0, 0
    while line < len(mapT):
        acc += 1 if mapT[line][column] == '#' else 0
        column += right - len(mapT[line]) if (column + right >=
                len(mapT[line])) else right
        line += down
    return acc

def main():
    with open("../input.txt") as f:
        inputL = [line.rstrip() for line in f]

    print(parse(inputL, 1, 1))
    print(parse(inputL, 3, 1))
    print(parse(inputL, 5, 1))
    print(parse(inputL, 7, 1))
    print(parse(inputL, 1, 2))

if __name__ == "__main__":
    main()
