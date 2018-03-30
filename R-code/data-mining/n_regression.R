setwd("path")
data<-read.csv("regression.csv",T)
data[]
x<-data[,1]
y<-data[,2]
plot(y~x)
x1<-x
x2<-x^2
x3<-x^3
lm.3<-lm(y~x1+x2+x3)   
summary(lm.3)
lines(x,fitted(lm.3))
plot(y~x)
lines(x,fitted(lm.3))    
point<-data.frame(x=1:10)
predict(lm.3,point,interval = "confidence",level=0.95)