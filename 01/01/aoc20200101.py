import os

def find2020():
    with open("input.txt") as f:
        input = [line.rstrip() for line in f]

    for n in input:
        ans = 2020 - int(n)
        if str(ans) in input:
            return(ans * int(n))

def main():
    print(find2020())

if __name__ == "__main__":
    main()
