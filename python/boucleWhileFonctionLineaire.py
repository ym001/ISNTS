#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pythonBoucleFonctionLineaire.py
#  
#  Ecrire un programme qui calcule la valeur d'une fonction lineaire 
#	pour les abscisses de valeurs 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
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
	print ("Calcul d'une fonction lineaire du type : y=a.x+b.\n")
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
	x=0
	while x<11:
		print ("\nx = "+str(x)+" : "+"y = "+str(fonction(x,a,b))+"\n")
		x=x+1

print ("   ---> Debut du programme.\n")
coefA,coefB=entree()
pourImpression(coefA,coefB)
print ("\n   ---> Fin du programme.")
