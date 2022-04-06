#NOM: NKOGO NSA
#PRENOM: MARCOS FLORENTINO
#MASTER-PYTHON-SUP INFO

"""C'est un programme avec un menu d'options, où nous pouvons
convertir l'heure en secondes et faire le contraire"""

def Convertir_A_seconde(h,m,s):
	return h * 3600 + m * 60 + s


def Convertir_A_HMS(sec):
	
	h = sec//3600
	sec = sec - h*3600
	m = sec//60
	sec = sec - m*60
	s = sec
	return h,m,s


while True:
	print("")
	print("1.- Convertir á secondes")
	print("2.- Convertir á heures, minutes y secondes")
	print("3.-Quitter")
	opcion = int(input())
	if opcion == 1:
		heure = int(input("Heures:"))
		minu = int(input("Minutes:"))
		sec = int(input("Secondes:"))
		print("Correspond á",Convertir_A_seconde(heure,minu,sec),"secondes.")
	elif opcion == 2:
		sec=int(input("Secondes:"))
		heure,minu,sec = Convertir_A_HMS(sec)
		print("Correspond á ",heure,"Heures:",minu,"min:",sec,"sec")
	
	elif opcion == 3:

		break
	else:
		print("OPTION: ERREUR")


