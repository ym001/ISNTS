mois_list=['janvier','fevrier']
jour_du_mois=[3,4]
jour_de_semaine=['lundi','mardi','mercredi']
for i,mois in enumerate(mois_list):
	nb_jour=jour_du_mois[i]
	jour=0
	while jour< nb_jour :
		print("Date : {} {}".format(mois,jour_de_semaine[jour%len(jour_de_semaine)]))
		jour+=1
