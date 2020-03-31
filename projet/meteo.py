#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  requete_http.py
#  
#  Copyright 2019 Mercadier <mercadier@mercadier>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  lien pour obtenir le clef : https://openweathermap.org/api


def main(args):
	import requests
	key=""
	ville="Nîmes"
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&appid="+key)
	data=r.json()
	print("Température de {} : {} °C".format(ville,data[u'main'][u'temp']-273.15))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
