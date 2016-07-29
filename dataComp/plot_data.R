#install.packages("plotly")
library(plotly)

# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)
# Convert to numerics
#argNums = as.numeric(myArgs)
#write to stdout stream
#cat(max(argNums))
myArgs

filename <- "updated_plate_reader.csv"
dat1 <- read.csv(filename)

source("grouping.R", echo = TRUE)

#find scope of data, y_range = maximum OD reading
#skip Time column
#y_max <- 0
#for (i in 2:length(dat1))
#{
#  #print(i)
#  if (max(dat1[[i]]) > y_max)
#  {
#    y_max <- max(dat1[[i]])
#  }
#}

