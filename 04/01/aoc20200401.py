import io

def parse(inputL):
    i, valid = 0, 0
    l = inputL.split('\n\n')
    for info in l:
        fieldCount = len(info.split())
        if fieldCount == 8 or (fieldCount == 7 and "cid" not in info):
            valid += 1
    return valid

def main():
    with open("../input.txt") as f:
        inputL = f.read()

    print(parse(inputL))

if __name__ == "__main__":
    main()
