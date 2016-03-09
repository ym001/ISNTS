#/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname() # Get local machine name# on bind notre socket 
port = 12345         # choix d'un port

sock.bind((host,port))
 
# On est a l'ecoute d'une seule et unique connexion :
sock.listen(1)
 
# Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
client, adresse = sock.accept() # accepte les connexions de l'exterieur
print "L'adresse",adresse,"vient de se connecter au serveur !"
message=""
# On est connecte, on fait une boucle d'inputs pour l'envoi des messages :
while message!="fin":
        RequeteDuClient = client.recv(255) # on recoit 255 caracteres grand max
        if not RequeteDuClient: # si on ne recoit plus rien
                break  # on break la boucle (sinon les bips vont se repeter)
        print RequeteDuClient,"\a"         # affiche les donnees envoyees, suivi d'un bip sonore
        message = raw_input('> ')  # on rentre des donnees
        client.send(message) # on envoie ces donnees
# fermer la connexion.
sock.close
