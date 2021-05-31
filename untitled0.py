import csv 

list_tmp=['Deepan','Saranya']
with open('First_pass.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(list_tmp)