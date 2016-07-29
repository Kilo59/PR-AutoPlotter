#plot_test_x.R
library(plotly)
#library(lubridate)
wd <- "C:/users/goreg/Google Drive//GitHub//data-alpha-Guilf//dataComp"
setwd(wd)
filename <- "updated_plate_reader.csv"
#setup data and data.frames
dat1 <- read.csv(filename)
time1 <- dat1$Time

###Testing Variables###
#group_list<- c(myArgs)
#group_list<- c('test4', 'test5', 'test6')
color_list<- c('black', 'red', 'blue', 'green', 'orange', 'purple', 'firebrick')
source('grouping.R')

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

g1<-ggplot() +
  geom_point(data = dat1, aes(time1, dat1$Well.Duh), color = 'red') +
  geom_point(data = dat1, aes(time1, dat1$Well_2), color = 'blue') +
  geom_point(data = dat1, aes(time1, dat1$Well_3), color = 'green') +
  labs(title = group_list[1], x= 'Time', y = 'Optical Density') +
  theme( axis.text.x=element_text(angle=80, size=7, vjust = 0.5) )
g1


image_name <- paste(group_list[1], '.png', sep = '')
ggsave(image_name, width = 22, height = 8)


df_list[2]

for (gl in group_list)
{
  print(gl)
}

test4
eval( as.name( paste('test4$','dat1.','Time', sep = '') ) )

for (gl in length(group_list))
{
  g<-ggplot() +
    geom_point( data = eval(as.name(gl)), aes(time1, df_list[[gl]][gl+1]) )
  
  image_name <- paste(group_list[gl], '.png', sep = '')
  ggsave(image_name, width = 22, height = 8)
}

ggplotly(g1)
