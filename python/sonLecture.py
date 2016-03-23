#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# script lecture.py
#  
#  Copyright 2016 Yves Mercadier
import pyglet

son = pyglet.media.load('son.wav', streaming=False)
son.play()

pyglet.app.run()
