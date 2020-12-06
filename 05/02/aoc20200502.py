import io

def decode(line):
    row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
    seat = (row,column)
    return seat

def getSeats(inputL):
    seats = []
    for line in inputL:
        row, column = decode(line)
        seats.append(row * 8 + column)
    return seats

def findMySeat(inputL):
    seats = getSeats(inputL)
    for seat in seats:
        if (seat + 2 in seats and seat + 1 not in seats):
            return seat + 1
        elif (seat - 2 in seats and seat - 1 not in seats):
            return seat - 1

def main():
    with open("../input.txt") as f:
        inputL = [line.rstrip() for line in f]

    print(findMySeat(inputL))

if __name__ == "__main__":
    main()
