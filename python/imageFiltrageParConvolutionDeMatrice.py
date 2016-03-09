#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#	Copyright 2015 Yves Mercadier
#	This program is free software; you can redistribute it and/or modify
#
#	Filtrage d’une image par étude des pixels voisins.
#	noyau de convolution	-1 -1 -1
#							-1  8 -1
#							-1 -1 -1
#
from PIL import Image
img = Image.open("image1.png")
largeur=img.size[0]
hauteur=img.size[1]
imgResultat = Image.new("RGB",(largeur,hauteur))

for y in range(1,hauteur-1):
	for x in range(1,largeur-1):
		pix0 = img.getpixel((x,y))
		pix1 = img.getpixel((x-1,y-1))
		pix2 = img.getpixel((x,y-1))
		pix3 = img.getpixel((x+1,y-1))
		pix4 = img.getpixel((x-1,y))
		pix5 = img.getpixel((x+1,y))
		pix6 = img.getpixel((x-1,y+1))
		pix7 = img.getpixel((x,y+1))
		pix8 = img.getpixel((x+1,y+1))
		r = 8*pix0[0]-pix1[0]-pix2[0]-pix3[0]-pix4[0]-pix5[0]-pix6[0]-pix7[0]-pix8[0]
		v = r
		b = r
		imgResultat.putpixel((x,y),(r,v,b))
imgResultat.show()
