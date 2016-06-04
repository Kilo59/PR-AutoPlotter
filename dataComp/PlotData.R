#set working directory
setwd("C:/Users/working_directory") #REPLACE

datA <- read.csv("columnA.csv")
datB <- read.csv("columnB.csv")

head(datA)
head(datB)

columnA <- datA$IntegerColumn
columnB <- datB$StringColumn

mean(columnA)
median(columnA)
hist(columnA)

plot(columnB)
