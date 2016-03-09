#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graphique1.py
#  
#  Copyright 2016 yves <yves.mercadier@ac-montpellier.fr>

from pylab import *

x = linspace(0, 2*pi, 30)
y = cos(x)

xlabel("abscisses")
ylabel("ordonnees")

title("Fonction cosinus")
plot(x, y,  "b:o")

savefig("cos.png")

show() # affiche la figure a l'ecran
