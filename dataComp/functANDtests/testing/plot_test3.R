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
Time1 <- hms(Time_char)
t1dur <- as.duration(Time1)
T1num <- as.numeric(Time1)
Time2 <- hour(Time1)*60 + minutes(Time1)
t2dur <- as.duration(Time2)
t2num <- as.numeric(Time2)


dTime2 <- as.POSIXct(Time_char, format = '%H:%M:%S')
dTime3 <- as.Time(dTime2)

?as.Date
?as.POSIXct
source("grouping.R", echo = TRUE)
?source()

dfTest <- data.frame(dat1$Time, dat1$Control, dat1$Well_2)
dfTest2 <- data.frame(t1dur, dat1$Control, dat1$Well_2)
dfTest3 <- data.frame(t2dur, dat1$Control, dat1$Well_2)

dat1_head <- head(dat1, n = 2L)
dat1_tail <- tail(dat1, n = 2L)

dat1_tail

y_range <- 0
for (column in 2:length(dat1)) {
  if (range(column) > y_range) y_range <- range(column)
}
xrange <- (dat1$Time)
yrange <- (data_range)

#qplot(x, y, data=, color=, shape=, size=, alpha=, geom=, method=, formula=, facets=, xlim=, ylim= xlab=, ylab=, main=, sub=)
#qplot(Group_32$Control, dat1$Time, data=Group_32, color='red', alpha=1/2, geom='line', xlim=xrange, ylim=yrange, xlab='Time', ylab='Optical Density', main='ggplot example')

ggplot(dat1) + geom_line()

ggplot(data = dfTest, aes(x = as.numeric(Time2), y = dfTest$dat1.Control) ) +
          geom_line() +
          geom_point(col = "red")

dfTest[2:3]

ggplot(data = dfTest, aes(x = as.numeric(t1dur), y = dfTest[2:2]) ) +
    geom_line() +
    geom_point(col = "blue", size = 0)

ggplot(data = dfTest) +
  geom_line() +
  geom_point( aes( x = as.numeric(t1dur), y = (dfTest[2:2])), col = "blue", size = 0)


image_name <- paste(Group_list[1], '.png', sep = '')
ggsave(image_name, width = 15, height = 15)

ggploty()
#######
# Simple Scatterplot
attach(dat1)
plot(Time, Control, main="Scatterplot Example",
  	xlab="Time", ylab="Optical Density ", type = "b")

#setwd(old_wd) #reset working directory
