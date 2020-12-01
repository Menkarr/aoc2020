import io

def find2020(input):
    for n in input:
        ans = 2020 - int(n) # on soustrait chaque nombre à 2020
        if str(ans) in input: # on vérifie si le résultat de la soustraction est présent dans la liste
            return(ans * int(n)) # s'il y est on a trouvé le résultat et il ne reste plus qu'à multiplier pour répondre à l'exercice

def findsubset_rec(input, i, target, mem):
    if i >= len(input) or target <= 0:
        return 1 if target == 0 else 0 # cas terminal, si la liste est vide le seul subset correct est 0
    if (i, target) not in mem:
        acc = findsubset_rec(input, i + 1, target, mem)
        acc += findsubset_rec(input, i + 1, target - int(input[i]), mem)
        mem[(i, target)] = acc # on stocke la valeur trouvée à ce niveau
    return mem[(i, target)]

def find3(input, target, mem):
    res = []
    for (i, num) in enumerate(input):
        tmp = findsubset_rec(input, i + 1, target - int(num), mem)
        if tmp > 0:
            res.append(num)
            target -= int(num)
    return res

def main():
    with open("input.txt") as f:
        input = [line.rstrip() for line in f] # on acquiert la liste d'inputs
    #print(find2020(input))

    mem = dict()
    #print(find3(["1","75","25","4","30","6","50","8","60","10"], 200, mem))
    print(find3(input, 2020, mem))

if __name__ == "__main__":
    main()
