#install.packages("plotly")
#install.packages('lubridate')
library(plotly)
library(lubridate)
old_wd <- getwd()
wd <- "C:/users/goreg/Google Drive//GitHub//data-alpha-Guilf//dataComp"
setwd(wd)

# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)
# Convert to numerics
#argNums = as.numeric(myArgs)
#write to stdout stream
#cat(max(argNums))
myArgs

filename <- "updated_plate_reader.csv"
#dat1_unlisted <- unlist( read.csv(filename) ) #unlist?
dat1 <- read.csv(filename)
datTime <- dat1$Time
Time_char <- as.character(datTime)
source("grouping.R", echo = TRUE)
###Testing Variables###
#group_list<- c(myArgs)
group_list<- c('test4', 'test5', 'test6')
df_list<- c()

image_name <- paste(Group_list[1], '.png', sep = '')
ggsave(image_name, width = 15, height = 15)


#######
# Simple Scatterplot
attach(dat1)
plot(Time, Control, main="Scatterplot Example",
  	xlab="Time", ylab="Optical Density ", type = "b")

#setwd(old_wd) #reset working directory
