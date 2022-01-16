#   This 

def solve():
    listExercises = input().split(";")

    nbre_exercices = 0

    for i in listExercises:
        if '-' in i:
            j = i.split("-")
            nbre_exercices += int(j[1]) - int(j[0]) + 1
        else:
            nbre_exercices += 1
            
    print(nbre_exercices)
    


if __name__ == '__main__':
    solve()
