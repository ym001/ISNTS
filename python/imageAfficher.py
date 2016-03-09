#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#	Copyright 2015 Yves Mercadier
#	This program is free software; you can redistribute it and/or modify
#
#	Charge un image et l'affiche
#
from PIL import Image
im = Image.open("image1.png")
print (im.format, im.size, im.mode)
im.show()
