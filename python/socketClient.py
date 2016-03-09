#/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket # on importe le module
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # on cree notre socket
 
# definition des informations :
host = socket.gethostname() # Get local machine name# on bind notre socket 
port = 12345         # choix d'un port

# on se connecte sur le serveur avec les informations ci-dessus
# assurez-vous d'avoir mis en marche le serveur !
sock.connect((host,port))
 
# On est connecte, on fait une boucle d'inputs pour l'envoi des messages :
message="Bonjour"
while message!="fin":
	sock.send(message) # on envoie ces donnees
	print sock.recv(1024)
	message = raw_input('> ')  # on rentre des donnees

# fermer la connexion.
sock.close
