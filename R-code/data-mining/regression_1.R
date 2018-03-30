setwd("path")    
data<-read.csv("regression.csv",T)    
plot(data[,1],data[,2])
x<-data[,1]
x
y<-data[,2]
y
lm.1<-lm(y~x)      
summary(lm.1)
abline(lm.1)     
point<-data.frame(x=2001:2010)
predict(lm.1,point,interval = "confidence",level=0.95) 