# -*- coding: utf-8 -*-
import csv
import sys
import os
import os.path

#definisco una funzione a cui fornisco la stringa che contiene il technical Debt come lo fornisce Sonar e mi restituisce il technical Debt in minuti
def minDebt(stringa):
	#creo delle variabili int per poterci poi lavorare
	giorni=0	
	minuti=0
	ore=0
	#nella stringa cerco la sottostringa d per individuare il giorno
	result=stringa.find('d')
	if(result!=-1):#la funzione find restituisce -1 quando non trova la sottostringa
		#verifico se il numero e' composto da due cifre, verificando se due caratteri dietro la d c'e' ancora un numero
		if(len(stringa)>1 and stringa[result-2].isdigit()):
			giorniS=stringa[result-2:result]#recupero una la sottostringa composta dalle due cifre
			giorni=int(giorniS)#faccio un cast della sottostringa a intero
		#verifico se il numero e' composto da una sola cifra come ho fatto prima
		elif(stringa[result-1].isdigit()):
			giorniS=stringa[result-1:result]#recupero una la sottostringa composta da una cifra
			giorni=int(giorniS)#faccio un cast della sottostringa a intero
	#nella stringa cerco la sottostringa h per individuare le ore e poi eseguo gli stessi controlli
	result=stringa.find('h')
	if(result!=-1):
		if(len(stringa)>1 and stringa[result-2].isdigit()):
			oreS=stringa[result-2:result]
			ore=int(oreS)
		elif(stringa[result-1].isdigit()):
			oreS=stringa[result-1:result]
			ore=int(oreS)
	#nella stringa cerco la sottostringa min per individuare i minuti e poi eseguo gli stessi controlli
	result=stringa.find('min')
	if(result!=-1):
		if(len(stringa)>1 and stringa[result-2].isdigit()):
			minutiS=stringa[result-2:result]
			minuti=int(minutiS)
		elif(stringa[result-1].isdigit()):
			minutiS=stringa[result-1:result]
			minuti=int(minutiS)
	#come valore di ritorno mi faccio dare la somma in minuti del tempo calcolato
	return int(giorni*8*60+ore*60+minuti)

class dato:
	#definisco le variabili che mi interessano
	versione=''
	filepath=''
	technicalDebt=0#in minuti
	#definisco una funzione per fare la stampa su csv
	def csvPrint(self):
        	string=[]
		string.append(self.versione)
		string.append(self.filepath)
		string.append(self.technicalDebt)
		return string

##############################################################################################
##################################Inizio elaborazione#########################################
##############################################################################################

#prendo il file txt con il technical debt da linea di comando
readpath = sys.argv[1]
#prendo il numero della versione da linea di comando
versione = sys.argv[2]

#Ottengo un array con le stringhe del file testuale di sonar
#with open("datiSonarV4.3.txt", "r") as f:
with open(readpath, "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
array = [x.strip() for x in content] 

#costruisco un array dove inseriro' una collezione di oggetti 
dati=[]
#parto dalla seconda riga del file n=1
n=1
while n<len(array):
	dat=dato()#creo un nuovo oggetto dato
	dat.versione=versione
	dat.filepath=array[n-1]#assegno al filepath il valore presente alla riga pari immediatamente precedente a quella di n
	dat.technicalDebt=minDebt(array[n])#mi faccio calcolare il technical debt con l'apposita funzione e lo inserisco nel dato
	dati.append(dat)#aggiungo il dato alla collezione di oggetti
	n+=2#ciclo solo sulle righe dispari

#costruisco il file csv
Resident_data = open('datiDebt'+versione+'.csv', 'w+')
csvwriter = csv.writer(Resident_data)
#creo l'head del file
file_head=[]
file_head.append("Versione")
file_head.append("File")	
file_head.append("TechinicalDebt(minuti)")
csvwriter.writerow(file_head)

#con un ciclo stampo tutti i dati dell'array
for index in range(0, len(dati)):
		csvwriter.writerow(dati[index].csvPrint())

#chiudo il file creato
Resident_data.close()
