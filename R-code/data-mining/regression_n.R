setwd("path")    
data<-read.csv("regression.csv",T)
data[]
y<-data[,1]
x1<-data[,2]
x2<-data[,3]
lm.2<-lm(y~x1+x2)     
summary(lm.2)
point<-data.frame(x=data[1,1]:data[13,1])
predict(lm.2,point,interval = "confidence",level=0.95)
