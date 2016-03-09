#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pythonFonctionParallelepipede.py
#  
#  Ecrivez un programme qui calcule le volume d'un parallelepipede rectangle dont sont
#  fournis au depart la largeur, la hauteur et la profondeur.
#
#  Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#  

#specifications
#parametre : 
#	aucun
#retour : 
#	a un nombre reel 
#	b un nombre reel 
def entree():
	#Les entrees du programme
	print ("Calcul d'une fonction linéaire'.\n")
	a = float(input("Indiquez la valeur de a :"))
	b = float(input("Indiquez la valeur de b :"))
	return a,b
	
#specifications
#Calcul d'une fonction lineaire
#parametre : 
#	x un nombre reel representant la valeur de l'abscisse'
#	a un nombre reel 
#	b un nombre reel 
#retour
#	y un nombre reel representant la valeur de l'ordonnee'
def fonction(x,a,b):
		y=  a*x+b
	return y

#specifications
#parametre : 
#	a un nombre reel 
#	b un nombre reel 
#retour
#	aucun
def pourImpression(a,b):
	for x in range(0,10)
		print ("\nx = "+x+" : "+"y = "+fonction(x,a,b)+"\n")

print ("   ---> Debut du programme.\n")
coefA,coefB=entree()
pourImpression(coefA,coefB)
print ("\n   ---> Fin du programme.")
