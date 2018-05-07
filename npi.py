#!/usr/bin/env python3

# Le programme avec la gestion des erreurs
import operator
from tkinter import *
  
root = Tk()
x0 = "0"
x1 = "1"
x2 = "2"
x3 = "3"
x4 = "4"
x5 = "5"
x6 = "6"
x7 = "7"
x8 = "8"
x9 = "9"
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
                op1 = resultat.pop()
                op2 = resultat.pop()
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


  
# ==== Functions ====
  #-----Prog Principal-----#

fen = Tk.Tk()
fen.title('Calculatrice')

fra1 = Frame(fen)
fra1.grid(row=1,column=0)
Button(fra1, text = '9', command= x9).grid(row=2, column = 2, padx = 3, pady = 3)
Button(fra1, text = '8', command= x8).grid(row=2, column = 1, padx = 3, pady = 3)
Button(fra1, text = '7', command= x7).grid(row=2, column = 0, padx = 3, pady = 3)
Button(fra1, text = '6', command= x6).grid(row=3, column = 2, padx = 3, pady = 3)
Button(fra1, text = '5', command= x5).grid(row=3, column = 1, padx = 3, pady = 3)
Button(fra1, text = '4', command= x4).grid(row=3, column = 0, padx = 3, pady = 3)
Button(fra1, text = '3', command= x3).grid(row=4, column = 2, padx = 3, pady = 3)
Button(fra1, text = '2', command= x2).grid(row=4, column = 1, padx = 3, pady = 3)
Button(fra1, text = '1', command= x1).grid(row=4, column = 0, padx = 3, pady = 3)
Button(fra1, text = '0', command= x0).grid(row=5, column = 2, padx = 3, pady = 3)

z = StringVar()
entree=Entry(fen,textvariable=z)
entree.grid(row=0,column=0)
z.set("0.")

Button(fra1, text= '+', command = aplus).grid(row=2,column=5, padx = 3, pady = 3)
Button(fra1, text= '-', command = amoins).grid(row=3,column=5, padx = 3, pady = 3)
Button(fra1, text= '*', command = afois).grid(row=2,column=6, padx = 3, pady = 3)
Button(fra1, text= '/', command = adiv).grid(row=3,column=6, padx = 3, pady = 3)
Button(fra1, text= '.', command = point).grid(row=4,column=5, padx = 3, pady = 3)
Button(fra1, text= '=', command = aegal).grid(row=4,column=6, padx = 3, pady = 3)
Button(fra1, text= 'C', command = clear).grid(row=5, column=6, padx = 3, pady = 3)
Button(fra1, text= 'Pile', command = pile).grid(row=7, column=7, padx = 3, pady = 3)

Button(fen,text='Quitter',command = fen.destroy).grid(row=6,column=7)
