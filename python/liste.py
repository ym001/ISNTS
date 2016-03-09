#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pythonListe.py
#  
#  Ecrivez un programme qui recherche le plus grand element present dans une liste d'entier positif donnee.
#
#  Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#  

#specifications
#Les entrees du programme
#parametre : 
#	aucun
#retour : 
#	l une liste d'entier 
def entree():
	l=[32, 5, 12, 8, 3, 75, 2, 15]
	return l
	
#specifications
#recherche du maximum d'une liste.
#parametre : 
#	l une liste d'entier
#retour
#	maximum un entier
def recherche(l):
	maximum=0
	for i in range(0,len(l)):
		if maximum<l[i]:
			maximum=l[i] 
	return maximum

#specifications
#parametre : 
#	m un nombre entier 
#retour
#	aucun
def pourImpression(m):
	print("le plus grand element de cette liste a la valeur "+str(m)+".")

print ("   ---> Debut du programme.\n")
liste=entree()
maximum=recherche(liste)
pourImpression(maximum)
print ("\n   ---> Fin du programme.")
