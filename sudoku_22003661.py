"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""
import random as random



grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""

def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,10):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def unique(x):
    """
    renvoie True si tous les éléments de x sont différents et False si au moins deux éléments de x sont identiques. A
    """
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]!=0 and x[j]!=0:
                if x[i]==x[j]:
                    return False       
    return True

def ligne(x, i):
    """
    Renvoie la ligne i de la grille de sudoku x
    """
    return x[i-1]

def colonne(x, i):
    """
    Renvoie la colonne i de la grille de sudoku x
    """
    s=[]
    for j in range(0,9):
        b=x[j][i-1]
        s.append(b)
    return s

def region(x, i):
    """
    Renvoie la region i de la grille de sudoku x
    """
    s=[]
    x_dep = (i%3)*3
    y_dep = (i//3)*3
    for l in range(y_dep, y_dep+3):
        for c in range(x_dep, x_dep+3):
            s.append(x[l][c])
    return s

def ajouter(x, i, j, v):
    """
    Ajoute la valeur v aux coordonnées (i, j) sur la grille de sudoku x
    """
    if x[i-1][j-1]==0 :
        l = x[i-1][j-1]
        x[i-1][j-1]=v
        k = 3 * ((i-1)//3) + ((j-1)//3)
        if unique(ligne(x,i)) and unique(colonne(x,j)) and unique(region(x,k)) :
            return x
        else :
            x[i-1][j-1]=l
            return x
    else :
        return x


def verifier(x):
    """
    Renvoie True si toutes les lignes, colonnes et régions de la grille sont valides et si la grille ne contient pas de 0, et False sinon
    """
    for p in range(0,len(x)):
        if unique(ligne(x,p)) and unique(colonne(x,p)) and unique(region(x,p)):
            for q in range(0,len(x)):
                if x[p][q]==0:
                    return False
        else :
            return False
    return True


def jouer(x):
    """
    Demande à l’utilisateur un triplet de valeurs (i, j, v) représentant une valeur v à placer aux coordonnées
    (i, j) sur la grille jusqu’à ce que la grille x soit entièrement remplie
    """
    afficher(x)
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]!=0 and x[j]!=0:
                a = int(input("Entrez une ligne entre 1 et 9: "))
                b = int(input("Entrez une colonne entre 1 et 9: "))
                c = int(input("Entrez la valeur souhaitée entre 1 et 9: "))
                ajouter(x,a,b,c)
                afficher(x)
    return afficher(x)


def solutions(x):
    """
    Renvoie un dictionnaire contenant les valeurs potentielles de chaque case vide de x
    """
    dico = {0:[] ,1:[] ,2:[] ,3:[] ,4:[] ,5:[] ,6:[] ,7:[] ,8:[] ,9:[]}
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            if x[i][j]==0:
                s = []
                for _ in range(1,10):
                    k = 3 * ((i)//3) + ((j)//3)
                    if _ not in ligne(x,i+1) and _ not in colonne(x,j+1) and _ not in region(x,k):
                        s.append(_)
                dico[len(s)].append((i,j,s))
    return dico


def resoudre(x):
    """
    Permet de résoudre une grille de sudoku x
    """
    dico = solutions(x)
    l = []
    for _ in list(dico.values()):
        for k in _ :
            if x[k[0]][k[1]] == 0:
                l.append(k)
    for b in range(len(l)):
        for t in l[b][2]:
            i = l[b][0]
            j = l[b][1]
            p = ajouter(x,i+1,j+1,t)
            q = resoudre(p)
            if type(q)==bool :
                x[i][j]=0
            else :
                return q
        return False
    if len(l)==0:
        return x
    for b in range(len(l)):
        if len(l[b][2])==0:
            return False

def generer(x):
    """
    Génere une grille de sudoku valide
    """
    dico = solutions(x)
    l = []
    for r in list(dico.values()):
        for k in r :
            if x[k[0]][k[1]] == 0:
                l.append(k)
    for b in range(len(l)):
        for t in l[b][2]:
            i = l[b][0]
            j = l[b][1]
            p = ajouter(x,i+1,j+1,t)
            a = sum([r.count(0) for r in x])
            if a >= 40 :
                for ligne in p:
                    random.shuffle(ligne)
            q = resoudre(p) 
            if type(q)==bool :
                x[i][j]=0
            else :
                return q
        return False
    if len(l)==0:
        return x
    for b in range(len(l)):
        if len(l[b][2])==0:
            return False


def nouvelle():
    """
    Crée une grille pleine et qui retire ensuite aléatoirement des valeurs de cette grille pleine avant de la renvoyer en tant que nouveau puzzle
    """
    x = generer(grille_0)
    a = 0
    while a <= 64:
        b = random.randint(0,8)
        c = random.randint(0,8)
        x[b][c]=0
        a = sum([ligne.count(0) for ligne in x])
    return x


jouer(nouvelle())
