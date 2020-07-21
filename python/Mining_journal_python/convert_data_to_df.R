# Getting author and affil

setwd("/Users/matthewmalishev/Documents/Manuscripts/2015/Pearson_etal")
journal<-read.csv("BioCons2.csv",header=F,sep=",")
colnames(journal)<-c("Author","Affil"); journal
head(journal)

BioCons<-read.csv("Biological Conservation.csv", header=T,sep=",")
#str(BioCons)
entry<-BioCons$C1
write.csv(entry, file = "BioCons_final.csv", row.names=F)

BioCons_final<-read.csv("BioCons_final.csv", header=T,sep=",")

# Getting publication year
setwd("/Users/matthewmalishev/Documents/Manuscripts/2015/Pearson_etal")

BioCons<-read.csv("Biological Conservation.csv",row.names=NULL,header=T ,sep=",")
#str(BioCons)
entry<-BioCons$PY
entry<-as.data.frame(entry)
head(entry)
write.csv(entry, file = "BioCons_PY.csv", row.names=F)
class(entry)



