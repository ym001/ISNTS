#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#	Copyright 2015 Yves Mercadier
#	This program is free software; you can redistribute it and/or modify
#
#	Acceder aux pixel d'une image'
#
from PIL import Image
img = Image.open("image1.png")
pixel = img.load()
largeur=img.size[0]
hauteur=img.size[1]
for x in range(largeur):    # pour tous les pixels
    for y in range(hauteur):
		rouge,vert,bleu=pixel[x,y]
		pixel[x,y]=(rouge,0,0)
img.show()
