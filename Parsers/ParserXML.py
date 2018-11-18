# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import csv
import sys
import os
import os.path

#A linea di comando inserire il file XLM, la versione del programma analizzato, il tipo di clone analizzato(1,2,3)
fileXML = sys.argv[1]
versione = sys.argv[2]
tipoClone = sys.argv[3]
#Costruisco l'albero a partire dal file xml dato in input
tree = ET.parse(fileXML)
root = tree.getroot()
#recupero il nome del sistema analizzato che poi aggiungero' ad ogni riga del file csv
attribut=root.find('systeminfo').attrib
system_name=[]
name=attribut["system"]
system_name.append(name)
#prepraro il file csv da fornire come output



#in questa versione creo un data.csv dove il parser invocato piu' volte ha modo di scrivere tutti i dati ricavati da diversi file xml

writepath = './data.csv'

#verifico l'esistenza del file
if(os.path.exists(writepath)):
	#se esiste lo apro in modalita' append e aggiungo i dati nuovi
	Resident_data = open(writepath,'a')
	csvwriter = csv.writer(Resident_data)
else:
	# altrimenti lo creo 
	Resident_data = open(writepath, 'w+')
	csvwriter = csv.writer(Resident_data)
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
	csvwriter.writerow(file_head)


'''
#In questa versione invece creo un file csv per ogni file xml analizzato
Resident_data = open(name+"-Type"+tipoClone+".csv", 'w')
csvwriter = csv.writer(Resident_data)
#creo la testa del file
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
csvwriter.writerow(file_head)
'''

#a partire dalla testa del file xml che è root cerco tutti i tag 'class'
for member in root.findall('class'):
    #per ogni tag di tipo class recupero il classID da aggiungere ai cloni corrispondenti
    attribute=member.attrib
    classID=attribute["classid"]
    similarity=attribute["similarity"]
    #per ogni tag di tipo class ricerco tutti i tag di tipo source e ne recupero gli attributi
    for member in member.findall('source'):
	attributes=member.attrib
	#recupero l'id univoco del clone
	pcid=attributes["pcid"]
	#recupero il file in cui e' presente il clone
	file=attributes["file"]
	#recupero la startline e la endline del codice clonato
	startline=attributes["startline"]
	endline=attributes["endline"]
	#eseguo la stampa sul file ad ogni cliclo del secondo for innestato in modo da avere una riga per ogni clone
    	csvwriter.writerow([name, versione, classID, pcid , file , startline , endline, tipoClone, similarity])
#una volta conclusi tutti i cicli proseguo a chiudere il file .csv
Resident_data.close()
