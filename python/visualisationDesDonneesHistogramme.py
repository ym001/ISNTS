#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  graphiqueHistogramme.py
#  
#  Copyright 2016 yves <yves.mercadier@ac-montpellier.fr>

import numpy as np
import pylab

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# ou x = [1, 3, 3, 3, 4, 5, 5, 8, 8, 8, 8, 9]

pylab.hist(x, bins=20)
pylab.show()
