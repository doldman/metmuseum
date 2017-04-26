
####################################################################################################################
#
#                                               How this program works#
#
#This program uses python csv reader to iterate through each row and colum of a csv file. Each colums is addressed as either a
#field that can simply use the header in (row[0]) to create an XML tag with the value as is, or do some normalisation.
# Normalisation is checked by type - e.g. Date normalisation, Dimension normalisation etc. The fields for these normalisation is currently hard
#coded into definitions that have a list of the fields. Normalisation appends the tree with the new tags.
#
#####################################################################################################################




import csv
import re
from lxml import etree as ET
from bs4 import BeautifulSoup

import nltk
import pandas
import normalise
##glossary http://mercury.lcs.mit.edu/~jnc/prints/glossary.html






##########################################  MAIN Starts HERE  #########################################





######   This opens and clears the file for appending  ###############
f = open('HokusaiMetObjects.csv','r',encoding='utf8')
w = open('hok.xml','w',encoding='utf8')
w.close()
w = open('hok.xml','a',encoding='utf8')

count = 0
rowcount = 0

#########    This reads as CSV    #######################################

myreader = csv.reader(f,delimiter=',')


############    This initiates an XML document for writing in the new elements from the CSV ####################

metDoc = ET.Element("metobject")

#############   This gets the first row which contans the header (firld names) ###########################

header = next(myreader)

#############   This gets the number of fields ###########################################

columns = len(header)

for row in myreader:
    rowcount += 1
    #print('row: ' + str(rowcount) )
    for i in range(0,columns):
        if normalise.isFieldforDateNormalisation(header[i]) == True:
            #print(header[i], row[i])
            normalise.DateNormalise(metDoc, header[i],row[i])
        elif normalise.isFieldforDimensionNormalisation(header[i]) == True:
            print(rowcount)
            normalise.DimensionNormalise(metDoc, header[i],row[i])
        elif normalise.isFieldforLanguageNormalisation(header[i]) == True and len(row[i].strip()) > 0:
            #print(header[i], row[i])
            normalise.LanguageNormalise(metDoc, header[i],row[i],'|')
        else:
            #print(row)
            #print('column: ' + str(i) + header[i])

            myfield = normalise.AddValueasXML(metDoc,header[i],row[i])

        if row[i] == "Katsushika Hokusai":
            normalise.AddExternalURIs(metDoc,'1820',row[i],"Person","BM")


myxml = ET.tostring(metDoc,pretty_print=True,method='xml',encoding='unicode')
print(BeautifulSoup(myxml, "xml").prettify(),file=w)
