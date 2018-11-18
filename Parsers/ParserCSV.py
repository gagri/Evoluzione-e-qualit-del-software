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
	
	#definisco un metodo che mi costruisce una stringa pronta per essere stampata su un csv
	def csvPrint(self):
        	string=[]
		string.append(self.project)
		string.append(self.version) 
		string.append(self.cloneClassID)
		string.append(self.pcid)
		result=self.filepath.find("src/")#mi assicuro di avere stampato il path dalla cartella src in poi e togliere tutto quello che c'e' prima
		string.append(self.filepath[result:])
		string.append(self.startline)
		string.append(self.endline)
		string.append(self.clonetype)
		string.append(self.similarity)
		return string

#A linea di comando inserire il file csv di partenza
#writepath = sys.argv[1]
writepath = 'data.csv'
Resident_data = open(writepath,'r')
#leggo il file csv e il contenuto viene inserito nel reader
csvreader = csv.reader(Resident_data)
#preparo un array che conterra' tutti i dati
dati=[]
for row in csvreader:
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
	#aggiungo il dato all'array
	dati.append(dat)

#inizio ad analizzare i dati ottenuti eliminando i cloni di tipo 1 e 2 classificati in maniera errata, ossia i cloni gia' classificati di tipo 1 riclassificati come tipo 2 o 3
#e faccio lo stesso tipo di controllo per i cloni di tipo 2 riclassificati come tipo 3
#utilizzo un doppio ciclo while per avere la possibilita' di modificare ad ogni ciclo la dimensione dell'array dati eliminando gli oggetti inutili
index=0
while index<len(dati):#ogni oggetto dell'array sara' confrontato con tutte le righe successive
	index2=index
	while index2<len(dati):
		#il confronto prendera' in esame solo alcuni campi che devono essere uguali tra i due dati considerati: versione, pcid, path, startline, endline e l'unico campo 			che deve essere diverso ossia il tipo del clone
		if(dati[index].version==dati[index2].version and dati[index].pcid==dati[index2].pcid and 
		dati[index].filepath==dati[index2].filepath and dati[index].startline==dati[index2].startline and 
		dati[index].endline==dati[index2].endline and dati[index].clonetype!=dati[index2].clonetype):
			dati.remove(dati[index2])#se l'if risulta vero l'oggetto viene eliminato dall'array
		index2+=1
	index+=1

#preparo un nuovo file csv da scrivere
Resident_data2 = open('datiParsati.csv', 'w+')
csvwriter = csv.writer(Resident_data2)
#con un ciclo stampo tutti i dati dell'array
for index in range(0, len(dati)):
		csvwriter.writerow(dati[index].csvPrint())

#chiudo i file utilizzati
Resident_data.close()
Resident_data2.close()

