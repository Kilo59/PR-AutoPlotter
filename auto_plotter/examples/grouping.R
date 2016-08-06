#file: grouping.R
#Time: 17:19:16
Group_16 <- data.frame(dat1$Time, dat1$Control, dat1$Well_41, dat1$Well_51, dat1$Well_61, dat1$Well_71)
Group_23 <- data.frame(dat1$Time, dat1$Control, dat1$Well_121, dat1$Well_151, dat1$Well_31)
Group_32 <- data.frame(dat1$Time, dat1$Control, dat1$Well_122, dat1$Well_31)
Group_4 <- data.frame(dat1$Time, dat1$Control, dat1$Well_31, dat1$Well_41)

####ggplots####
g1 <- ggplot()+
geom_point(data = dat1, aes(Time, dat1$Control), color = 'black') +
geom_point(data = dat1, aes(Time, dat1$Well_41), color = 'red') +
geom_point(data = dat1, aes(Time, dat1$Well_51), color = 'blue') +
geom_point(data = dat1, aes(Time, dat1$Well_61), color = 'orange') +
geom_point(data = dat1, aes(Time, dat1$Well_71), color = 'green') +
labs(title = 'Group_16', x= 'Time', y = 'Optical Density') +
theme( axis.text.x= element_text(angle = 80, size = 7, vjust = 0.7) )

image_name <- paste('Group_16', '.png', sep = '')
ggsave(image_name, width = 22, height = 8)

g2 <- ggplot()+
geom_point(data = dat1, aes(Time, dat1$Control), color = 'black') +
geom_point(data = dat1, aes(Time, dat1$Well_121), color = 'red') +
geom_point(data = dat1, aes(Time, dat1$Well_151), color = 'blue') +
geom_point(data = dat1, aes(Time, dat1$Well_31), color = 'orange') +
labs(title = 'Group_23', x= 'Time', y = 'Optical Density') +
theme( axis.text.x= element_text(angle = 80, size = 7, vjust = 0.7) )

image_name <- paste('Group_23', '.png', sep = '')
ggsave(image_name, width = 22, height = 8)

g3 <- ggplot()+
geom_point(data = dat1, aes(Time, dat1$Control), color = 'black') +
geom_point(data = dat1, aes(Time, dat1$Well_122), color = 'red') +
geom_point(data = dat1, aes(Time, dat1$Well_31), color = 'blue') +
labs(title = 'Group_32', x= 'Time', y = 'Optical Density') +
theme( axis.text.x= element_text(angle = 80, size = 7, vjust = 0.7) )

image_name <- paste('Group_32', '.png', sep = '')
ggsave(image_name, width = 22, height = 8)

g4 <- ggplot()+
geom_point(data = dat1, aes(Time, dat1$Control), color = 'black') +
geom_point(data = dat1, aes(Time, dat1$Well_31), color = 'red') +
geom_point(data = dat1, aes(Time, dat1$Well_41), color = 'blue') +
labs(title = 'Group_4', x= 'Time', y = 'Optical Density') +
theme( axis.text.x= element_text(angle = 80, size = 7, vjust = 0.7) )

image_name <- paste('Group_4', '.png', sep = '')
ggsave(image_name, width = 22, height = 8)

####plotly####
#Sys.setenv("plotly_username" = "your_username")
#Sys.setenv("plotly_username" = "your_api_key")
plot_list <-c('g1', 'g2', 'g3', 'g4')
#for (plot in plot_list)
#{
#	plotly_POST( eval(as.name(plot)), plot )
#}
