# -*- coding: utf-8 -*-
import csv
import sys
import os
import os.path


class dato:
	#definisco le variabili che mi interessano
	versione=''
	filepath=''
	technicalDebt=0#in minuti
	smells=0
	#definisco una funzione per fare la stampa su csv
	def csvPrint(self):
        	string=[]
		string.append(self.versione)
		string.append(self.filepath)
		string.append(self.technicalDebt)
		string.append(self.smells)
		return string

##############################################################################################
##################################Inizio elaborazione#########################################
##############################################################################################

#A linea di comando inserire il file csv di partenza
writepath = sys.argv[1]
#writepath = 'datiDebt.csv'
Resident_data = open(writepath,'r')
#leggo il file csv e il contenuto viene inserito nel reader
csvreader = csv.reader(Resident_data)

#preparo un array che conterra' tutti i dati
dati=[]
for row in csvreader:
		if(row[0]!='Versione'):
			#per ogni riga del reader creo un nuovo dato
			dat=dato()
			#assegno i valori delle variabili del dato recuperandoli dal reader
			dat.versione=row[0]
			dat.filepath=row[1]
			dat.technicalDebt=row[2]
			dati.append(dat)

#A linea di comando inserire il file txt che contiene gli smell
readpath = sys.argv[2]
#Ottengo un array con le stringhe del file testuale di sonar
#with open("codesmell4.3.txt", "r") as f:
with open(readpath, "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
array = [x.strip() for x in content] 

#parto dalla seconda riga del file n=1
n=1
while n<len(array):
	m=0
	while m<len(dati):
		if(dati[m].filepath==array[n-1]):
			dati[m].smells=array[n]
			m=len(dati)+1
		m+=1
	n+=2#ciclo solo sulle righe dispari


writepath = 'datiDebtSmell.csv'

#verifico l'esistenza del file
if(os.path.exists(writepath)):
	#se esiste lo apro in modalita' append e aggiungo i dati nuovi
	Resident_data2 = open(writepath,'a')
	csvwriter = csv.writer(Resident_data2)
else:
	# altrimenti lo creo 
	Resident_data2 = open(writepath, 'w+')
	csvwriter = csv.writer(Resident_data2)
	#creo la testa del file e la aggiungo
	file_head=[]
	file_head.append("Versione")
	file_head.append("File")	
	file_head.append("TechinicalDebt(minuti)")
	file_head.append("CodeSmell")
	csvwriter.writerow(file_head)

#con un ciclo stampo tutti i dati dell'array
for index in range(0, len(dati)):
		csvwriter.writerow(dati[index].csvPrint())

#chiudo il file creato
Resident_data.close()
Resident_data2.close()
