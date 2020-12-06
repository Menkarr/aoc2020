import io

def isValidNew(password): # password est une string au format 'x-y z: pass'
    word = password.split(' ')
    x,y = int(word[0].split('-')[0]) - 1, int(word[0].split('-')[1]) - 1 # x-y représente l'intervalle du nombre de fois où on doit retrouver z dans pass
    z = word[1].rstrip(':')
    return ((word[2][x] == z) ^ (word[2][y] == z)) # renvoie 1 si valide

def countValid(inputL): # inputL est une liste de passwords (un par ligne)
    acc = 0
    for password in inputL: # on itère isValid sur toute la liste en utilisant un accumulateur pour compter les entrées valides
        acc += isValidNew(password)
    return acc # on renvoie l'accumulateur

def main():
    with open("../input.txt") as f:
        inputL = [line.rstrip() for line in f] # on acquiert la liste d'inputs

    print(countValid(inputL))

if __name__ == "__main__":
    main()
