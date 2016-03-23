#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# script son1.py
#  
#  Copyright 2016 Yves Mercadier

import wave
import math


nbCanal = 1   
nbOctet = 1    # taille d'un échantillon : 1 octet = 8 bits
frequenceEchantillonnage = 44100   
frequence = 1000
duree = 1
amplitude = 100
nbEchantillon = duree*frequenceEchantillonnage

# ouverture du fichier en écriture
son = wave.open('son.wav','w') 

# création de l'en-tête (44 octets)
parametres = (nbCanal,nbOctet,frequenceEchantillonnage,nbEchantillon,'NONE','not compressed')# tuple
son.setparams(parametres)    

# calcul de tous les échantillons
for i in range(0,nbEchantillon):
    pulsation=2.0*math.pi*frequence/frequenceEchantillonnage
    val = wave.struct.pack('B',int(127.5 + amplitude*math.sin(pulsation*i)))
    son.writeframes(val) 

# fermeture du fichier
son.close()
