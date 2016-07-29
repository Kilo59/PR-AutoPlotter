#install.packages("plotly")
library(plotly)
Sys.setenv("plotly_username"= " ") #add plotly account username 
Sys.setenv("plotly_api_key"= " ") #add plotly accound api key
# Fetch command line arguments
myArgs <- commandArgs(trailingOnly = TRUE)
#write to stdout stream
#cat()
myArgs

filename <- "updated_plate_reader.csv"
dat1 <- read.csv(filename)

source("grouping.R", echo = TRUE)

for (plot in plot_list)
{
  print(plot)
  plotly_POST( eval(as.name(plot)), plot )
}

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

