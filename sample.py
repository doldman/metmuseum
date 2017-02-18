import csv
import re



f = open('metmuseum.csv','r',encoding='utf8')
w = open('randommet.csv','w',encoding='utf8')
w.close()
w = open('randommet.csv','a',encoding='utf8')

myreader = csv.reader(f,delimiter=',')
mywriter = csv.writer(w)
count = 0
for row in myreader:
    count += 1
    if count%100 == 0:
        mywriter.writerow(row)
        print(row)

w.close()