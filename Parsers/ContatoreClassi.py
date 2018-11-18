# -*- coding: utf-8 -*-
import csv
import sys
import os
import os.path

#definisco un oggetto che mi rappresenta il dato clone
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
	recurrence=0#valore di default della ricorrenza di un file
	newPath=0#valore di default e' 0, utilizzo una codifica numerica per poter fare poi la somma su excel
	
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
		string.append(self.recurrence)
		string.append(self.newPath)
		return string

#A linea di comando inserire il file csv di partenza
#writepath = sys.argv[1]
writepath = 'datiFinali.csv'
Resident_data = open(writepath,'r')
#leggo il file csv e il contenuto viene inserito nel reader
csvreader = csv.reader(Resident_data)
#preparo un array che conterra' tutti i dati
dati=[]
for row in csvreader:
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
		dat.technicalDebt=row[9]
		dat.smells=row[10]
		#aggiungo il dato all'array
		dati.append(dat)

#eseguo un doppio ciclo sui dati ottenuti andando a verificare di volta in volta se ho gia' incontrato quel file oppure no tra i cloni
index=0
while index<len(dati):#ogni oggetto dell'array sara' confrontato con tutte le righe successive
	#se l'oggetto ha un file path mai visto prima allora la sua ricorrenza sara' quella di dafault 0, inoltre mi assicuro di non fare questo controllo sui file che non 		hanno cloni
	if dati[index].cloneClassID!='0' and dati[index].cloneClassID !=0 and dati[index].recurrence==0 : 
		dati[index].recurrence=1#aggiorno ad 1 la ricorrenza
 		dati[index].newPath=1#porto ad 1 il valore che mi indica che questo e' un nuovo path
	#eseguo il secondo ciclo a partire dall'oggetto successivo a quello appena analizzato
	index2=index+1
	#il ciclo deve continuare fino alla fine dell'array che contiene i dati, oppure se il dato in analisi ha un path che e' gia stato trovato e considerato in un ciclo 		precedente, nel secondo caso uso un valore di segnalazione -1
	while index2<len(dati) and dati[index].recurrence!=-1 :
		#il confronto prendera' in esame solo alcuni campi che devono essere uguali tra i due dati considerati: versione e path. Assicurandosi comunque di evitare di 			#fare questi contretti a fare questi controlli se si stanno analizzando classi e non cloni.
		if dati[index].cloneClassID !='0' and dati[index].cloneClassID !=0 and dati[index].version==dati[index2].version and dati[index].filepath==dati[index2].filepath :
			#se il path corrisponde viene aumentata la ricorrenza del clone che si e' incontrato per primo  
			dati[index].recurrence+=1
			#mentre viene settata a -1 la ricorrenza di tutti i cloni incrontati nel secondo ciclo while, in modo da marchiarli come gia' analizzati ed evitare di 				#riconsiderarli nuovamente nel primo ciclo while
			dati[index2].recurrence=-1
		index2+=1
	index+=1


#preparo un nuovo file csv da scrivere
Resident_data2 = open('datiFinaliOccorrenze.csv', 'w+')
csvwriter = csv.writer(Resident_data2)
#creo l'head del file
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
file_head.append("recurrence")
file_head.append("newPath")
csvwriter.writerow(file_head)

#con un ciclo stampo tutti i dati dell'array
for index in range(0, len(dati)):
		csvwriter.writerow(dati[index].csvPrint())

#chiudo i file utilizzati
Resident_data.close()
Resident_data2.close()

