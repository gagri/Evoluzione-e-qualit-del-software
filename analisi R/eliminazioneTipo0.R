fast<-read.table("AnalisiFastJson_no_tipo_0.csv", header=TRUE, sep=";")
kruskal.test(fast$len~fast$type)
library(gplots)
plotmeans(len~type, data=fast,  main="Analisi Lunghezza Cloni (LOC)", xlab="Tipo di clone", ylab="Lunghezza Cloni (LOC)", frame=FALSE)


#tipo/smell
#tipo/smell
#tipo/dim clone (smell)
