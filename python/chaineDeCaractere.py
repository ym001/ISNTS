#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pythonChaineDeCaractere.py
#  
#  Ecrire un script qui determine si une chaine contient ou non le caractere e.
#
#  Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#  

#specifications
#Les entrees du programme
#parametre : 
#	aucun
#retour : 
#	ch une chaine de caractere 
def entree():
	print ("Recherche d'un caractere dans un texte.\n")
	ch =raw_input("Ecrivez un texte :")
	return ch
	
#specifications
#recherche du caractere 'e' dans ch.
#parametre : 
#	ch une chaine de caractere
#retour
#	true si le caractere 'e' est dans le texte
#	false si le caractere 'e'n'est pas dans le texte
def recherche(ch):
	t=False
	for i in range(0,len(ch)):
		if "e"==ch[i]:
			t=True 
	return t

#specifications
#parametre : 
#	t un booleen 
#retour
#	aucun
def pourImpression(t):
	if t:
		print("le texte contient le caractere 'e'.")
	else:
		print("le texte ne contient pas le caractere 'e'.")

print ("   ---> Debut du programme.\n")
texte=entree()
test=recherche(texte)
pourImpression(test)
print ("\n   ---> Fin du programme.")
