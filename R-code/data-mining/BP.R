library(grid)   
library(MASS)
library(neuralnet)
p <- matrix(c(80.0,90.0,180.0,140.0,120.0,3.0,8.0,20.0,16.0,5.0,50.0,70.0,120.0,90.0,85.0),5,3,byrow = T)
t <- c(11.0,12.5,20.0,18.0,15.5)
trainingdata <- cbind(p,t) 
trainingdata
colnames(trainingdata) <- c("Input1","Input2","Input3","Output")
net <- neuralnet(Output~Input1+Input2+Input3,trainingdata, hidden=20, threshold=0.001)   
print(net)   
plot(net)   
testdata <- trainingdata[,1:3]  
net.results <- compute(net, testdata)   
ls(net.results)   
print(net.results$net.result) 
cleanoutput <- cbind(testdata,trainingdata[,4],as.data.frame(net.results$net.result))   
colnames(cleanoutput) <- c("Input1","Input2","Input3","Expected Output","Neural Net Output")   
print(cleanoutput)   

