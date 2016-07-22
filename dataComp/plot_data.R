#install.packages("plotly")
library(plotly)
old_wd <- getwd()
wd <- "C:/Users/goreg/OneDrive/Documents/GitHub/data-alpha-Guilf/dataComp"
setwd(wd)

# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)
# Convert to numerics
#argNums = as.numeric(myArgs)
#write to stdout stream
#cat(max(argNums))
myArgs

filename <- "updated_plate_reader.csv"
dat1_unlisted <- unlist( read.csv(filename) ) #unlist?
dat1 <- read.csv(filename)
source("grouping.R")

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



#######
# Simple Scatterplot
attach(dat1)
plot(Time, Control, main="Scatterplot Example", 
  	xlab="Time", ylab="Optical Density ", type = "b")

#setwd(old_wd) #reset working directory