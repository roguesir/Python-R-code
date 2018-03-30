library("httr")
library("XML")
library("stringr")
library("ggplot2")

# Define image source
img.url = 'https://assets.donaldjtrump.com/site/about_body_img_2.jpg'

# Define Microsoft API URL to request data
URL.emoface = 'https://api.projectoxford.ai/emotion/v1.0/recognize'

# Define access key (access key is available via: https://www.microsoft.com/cognitive-services/en-us/emotion-api)
emotionKEY = '89b3bff2899448c399ca0894d48256cc'

mybody = list(url = img.url)

# Request data from Microsoft
faceEMO = POST(
  url = URL.emoface,
  content_type('application/json'), add_headers(.headers = c('Ocp-Apim-Subscription-Key' = emotionKEY)),
  body = mybody,
  encode = 'json'
)

# Show request results (if Status=200, request is okay)
faceEMO

# Reuqest results from face analysis
Obama = httr::content(faceEMO)[[1]]
Obama
# Define results in data frame
o<-as.data.frame(as.matrix(Obama$scores))

# Make some transformation
o$V1 <- lapply(strsplit(as.character(o$V1 ), "e"), "[", 1)
o$V1<-as.numeric(o$V1)
colnames(o)[1] <- "Level"

# Define names
o$Emotion<- rownames(o)

# Make plot
ggplot(data=o, aes(x=Emotion, y=Level)) +
  geom_bar(stat="identity")

#####################################################################
# Define image source
img.url = 'https://assets.donaldjtrump.com/site/about_body_img_2.jpg'

# Define Microsoft API URL to request data
faceURL = "https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=age"

# Define access key (access key is available via: https://www.microsoft.com/cognitive-services/en-us/face-api)
faceKEY = 'ec851ed8ae194c8ab6b4c7ab0bd95a35'

# Define image
mybody = list(url = img.url)

# Request data from Microsoft
faceResponse = POST(
  url = faceURL, 
  content_type('application/json'), add_headers(.headers = c('Ocp-Apim-Subscription-Key' = faceKEY)),
  body = mybody,
  encode = 'json'
)

# Show request results (if Status=200, request is okay)
faceResponse

# Reuqest results from face analysis
ObamaR = httr::content(faceResponse)[[1]]

# Define results in data frame
OR<-as.data.frame(as.matrix(ObamaR$faceLandmarks))

# Make some transformation to data frame
OR$V2 <- lapply(strsplit(as.character(OR$V1), "\\="), "[", 2)
OR$V2 <- lapply(strsplit(as.character(OR$V2), "\\,"), "[", 1)
colnames(OR)[2] <- "X"
OR$X<-as.numeric(OR$X)

OR$V3 <- lapply(strsplit(as.character(OR$V1), "\\y = "), "[", 2)
OR$V3 <- lapply(strsplit(as.character(OR$V3), "\\)"), "[", 1)
colnames(OR)[3] <- "Y"
OR$Y<-as.numeric(OR$Y)

OR$V1<-NULL
OR
