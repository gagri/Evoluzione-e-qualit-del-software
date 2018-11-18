# -*- coding: utf-8 -*-
import csv
import sys
import os
import os.path

#definisco un oggetto che mi rappresenta il dato
class dato:
	#definisco le variabili che mi interessano
	project=""
	version=""
	cloneClassID=0
	pcid=0
	filepath=""
	startline=0
	endline=0
	clonetype=0
	similarity=0
	technicalDebt=0
	smells=0
	
	
	#definisco un metodo che mi costruisce una stringa pronta per essere stampata su un csv
	def csvPrint(self):
        	string=[]
		string.append(self.project)
		string.append(self.version) 
		string.append(self.cloneClassID)
		string.append(self.pcid)
		string.append(self.filepath)
		string.append(self.startline)
		string.append(self.endline)
		string.append(self.clonetype)
		string.append(self.similarity)
		string.append(self.technicalDebt)
		string.append(self.smells)
		return string


##############################################################################################
##################################Inizio elaborazione#########################################
##############################################################################################


#A linea di comando inserire i file csv di partenza
#pathNicad = sys.argv[1]
pathNicad= 'datiParsati.csv'
Resident_data = open(pathNicad,'r')
#leggo il file csv e il contenuto viene inserito nel reader
nicadReader = csv.reader(Resident_data)

#pathSonar = sys.argv[2]
pathSonar= 'datiDebtSmell.csv'
Resident_data2 = open(pathSonar,'r')
#leggo il file csv e il contenuto viene inserito nel reader
sonarReader = csv.reader(Resident_data2)

#Creo due array uno conterra' le classi che contengono cloni, l'altro le classi che non contengono cloni
classiConCloni=[]
classiSenzaCloni=[]

#recupero tutti i cloni che mi ha fornito nicad con i relativi dati
for row in nicadReader:
	if(row[0]!='project'):
		#per ogni riga del reader creo un nuovo dato
		dat=dato()
		#assegno i valori delle variabili del dato recuperandoli dal reader
		dat.project=row[0]
		dat.version=row[1]
		dat.cloneClassID=row[2]
		dat.pcid=row[3]
		dat.filepath=row[4]
		dat.startline=row[5]
		dat.endline=row[6]
		dat.clonetype=row[7]
		dat.similarity=row[8]
		classiConCloni.append(dat)

#Inizio ad analizzare il file contenente tutte le classi che mi ha fornito sonar
for row2 in sonarReader:
	if(row2[0]!='Versione'):
		#anche in questo caso creo un dato temporaneo che riempio con i dati recuperati dal file, lasciando gli altri di default
		dat=dato()
		dat.version=row2[0]
		dat.filepath=row2[1]
		dat.technicalDebt=row2[2]
		dat.smells=row2[3]
		#variabile per la gestione del ciclo while da effettuare sull'array dei dati ottenuti da nicad
		i=0
		while i<len(classiConCloni):
			#ricerco all'interno della collezione di cloni, un clone che abbia lo stesso filepath di quello che sto analizzando adesso dal file ottenuto da sonar
			#cosi' da porter aggiungere al dato contenuto all'interno dell'array classiConCloni le informazioni relative a technical debt e smell che fanno 			#riferimento alla classe, dove si trova il clone
			if(classiConCloni[i].version==dat.version and classiConCloni[i].filepath==dat.filepath):#verifico se la versione e il path dei due file corrisponde
				classiConCloni[i].technicalDebt=dat.technicalDebt
				classiConCloni[i].smells=dat.smells
				dat.cloneClassID=classiConCloni[i].cloneClassID
			i+=1
		#se il file non fa parte riferimento a nessun clone, vuol dire che non ne contiene e allora l'aggiungo alla collezione classiSenzaCloni
		if(dat.cloneClassID==0 or dat.cloneClassID=='0'):
			classiSenzaCloni.append(dat)


# altrimenti lo creo 
Resident_data3 = open('datiFinali.csv', 'w+')
csvwriter = csv.writer(Resident_data3)
#creo la testa del file e la aggiungo
file_head=[]
file_head.append("project")	
file_head.append("version")
file_head.append("CloneClassID")
file_head.append("pcid")
file_head.append("file")
file_head.append("startline")
file_head.append("endline")
file_head.append("type")
file_head.append("similarity")
file_head.append("TechinicalDebt(minuti)")
file_head.append("CodeSmell")
csvwriter.writerow(file_head)



#con un ciclo stampo tutti i dati dell'array classiConCloni
for index in range(0, len(classiConCloni)):
		csvwriter.writerow(classiConCloni[index].csvPrint())

#con un ciclo stampo tutti i dati dell'array classiSenzaCloni
for index in range(0, len(classiSenzaCloni)):
		csvwriter.writerow(classiSenzaCloni[index].csvPrint())

#chiudo i file utilizzati
Resident_data.close()
Resident_data2.close()
Resident_data3.close()

