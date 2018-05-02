#!/usr/bin/env python3

# Le même programme avec la gestion des erreurs
import operator

operateurs = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv,
             "^": pow}

def _read():
    try:
        expr = input("> ").split()
        if len(expr) == 0:
            raise EOFError
    except EOFError:
        exit()
    return expr

def _eval(expr):
    resultat = []
    erreur = False
    for w in expr:
        if w in operateurs.keys():
            try:
                op1 = result.pop()
                op2 = result.pop()
            except IndexError:
                print("Erreur : Trop peut d'opérande pour l'opération "+w)
                erreur = True
                break
            resultat.append(operateurs[w](op2,op1))
        else:
            try:
                resultat.append(float(w))
            except ValueError:
                print("Erreur : "+w+" ce n'est pas un nombre")
                erreur = True
                break
    return resultat if not erreur else None

def _print(resultat):
    if resultat:
        if len(resultat) == 1:
            print(resultat[0])
        else:
            print("Erreur : trop peu d'opérateurs")

if __name__ == "__main__":
    while True:
        _print(_eval(_read()))
