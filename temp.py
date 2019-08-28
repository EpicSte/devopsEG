#!/usr/bin/env python3
# programme temperature.py
#super steven on est la !!!!ouioui

try:
    temp=int(input("Quelle température fait-il ? "))
except ValueError:
    print("la valeur entrée n'est pas numerique")
else:
    if int(temp)> 18 :
        print("Il fait beau !")
    else:
        print("Il fait un peu frais, non ?")
