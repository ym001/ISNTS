#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pythonPremierTest.py
#  
#  Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#  


#Les entrees du programme
#specifications
#parametre : 
#	aucun
#retour : 
#	a un nombre entier representant l'age de la personne.

def entree():
	#Les entrees du programme
	print ("Aurez-vous l'age de conduire une voiture en 2015 ?\n")
	a = int(input("Quelle est ton annee de naissance? "))
	return a
	
#Calcul de l'age de la personne'
#specifications
#parametre : 
#	d un nombre entier representant la date de naissance
#retour
#	a un nombre entier represantant l'age de la personne 
def metier(d):
	#le calcul
	a=2015-d  
	return a

#Affichage
#specifications
#parametre : 
#	a un nombre entier represantant l'age de la personne 
#retour
#	aucun
def pourImpression(v):
	strImpression="";""
	if age>18:
		strImpression="\nEn 2015 tu pourras conduire une voiture :-)"
	else:
		strImpression="\nEn 2015 tu ne pourras pas conduire une voiture. Desole..."
	return strImpression;


print ("   ---> Debut du programme.\n")
annee=entree()
age=metier(annee)
print(pourImpression(age))
print ("\n   ---> Fin du programme.")
