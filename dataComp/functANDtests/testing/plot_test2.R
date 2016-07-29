library(plotly)
library(lubridate)
wd <- "C:/users/goreg/Google Drive//GitHub//data-alpha-Guilf//dataComp"
setwd(wd)

filename <- "updated_plate_reader.csv"

#setup data and data.frames
dat1 <- read.csv(filename)
time1 <- dat1$Time
dat2 <- data.frame(time2 = time1, d1 = dat1$Well.Duh, d2 = dat1$Well_2)
d3 <- dat1$Well_2
d_list <- c(dat2, d3)
#SetupTime
Time_char <- as.character(dat1$Time)
Time1 <- hms(Time_char)
Time2 <- hour(Time1)*60 + minutes(Time1)
T2num <- as.numeric(Time2)
#represent command line args from python
group_list <- c('test1', 'test2', 'test3')


#find scope of data, y_range = maximum OD reading
#skip Time column
y_max <- 0
for (i in 2:length(dat1)) 
{
  #print(i)
  if (max(dat1[[i]]) > y_max) 
    {
       y_max <- max(dat1[[i]])
    }
}

#########ggplot testing###################
#test1
g<-ggplot( dat2, aes(T1num, dat1$Well.Duh) ) +
    geom_point(color = 'firebrick')
g<- g+ ylim(c(0, y_max))
g
image_name <- paste(group_list[1], '.png', sep = '')
ggsave(image_name, width = 15, height = 15)

T1num
#g<-ggplot(dat2, aes(time2, d1)) +
#  geom_point(color = 'firebrick') +
#  geom_point(data = d3, color = 'blue')