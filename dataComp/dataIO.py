#dataIO
import csv
#Input/Output
def singleCol_CSV(filename, header, item_list):
    with open(filename, 'w', newline='') as csvfile:
        writer1 = csv.writer(csvfile, delimiter= ',')
        writer1.writerow([header])
        for i in range(len(item_list)):
            writer1.writerow([item_list[i]])
    return


#Columns must be past be passed in as a list of lists, each with the same length
def doubleCol_CSV(filename, header_list, list_of_columns):
    with open(filename, 'w', newline='') as csvfile:
        writer2 = csv.writer(csvfile, delimiter=',')
        if len(list_of_columns[0]) != len(list_of_columns[1]):
            print("ERROR: Columns must have the same number of items")
            writer2.writerow( ['ERROR: Columns must have the same number of items'] )
        else:
            writer2.writerow([header_list[0], header_list[1]])
            for i in range(len(list_of_columns[0])):
                writer2.writerow([ list_of_columns[0][i],list_of_columns[1][i] ])
    return
