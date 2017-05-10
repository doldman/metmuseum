
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



#############   This gets the first row which contans the header (firld names) ###########################

header = next(myreader)

#############   This gets the number of fields ###########################################

columns = len(header)

met = ET.Element("met")

for row in myreader:


    rowcount += 1
    globals()['metDoc' + str(rowcount)] = ET.SubElement(met, "metobject")

    #print('row: ' + str(rowcount) )
    for i in range(0,columns):

        #print(rowcount)

        if normalise.isFieldforDateNormalisation(header[i]) == True:
            #print(header[i], row[i])
            normalise.DateNormalise(globals()['metDoc' + str(rowcount)], header[i],row[i])
        elif normalise.isFieldforDimensionNormalisation(header[i]) == True:
            normalise.DimensionNormalise(globals()['metDoc' + str(rowcount)], header[i],row[i])
        elif normalise.isFieldforLanguageNormalisation(header[i]) == True and len(row[i].strip()) > 0:
            #print(header[i], row[i])
            normalise.LanguageNormalise(globals()['metDoc' + str(rowcount)], header[i],row[i],'|')
        elif normalise.isFieldforPeriod(header[i]) == True:
            #print(row[i])
            normalise.PeriodNormalise(globals()['metDoc' + str(rowcount)],header[i],row[i])
        elif normalise.isMedium(header[i]) == True:
            #print(row[i])
            normalise.typetechniqueNormalise(globals()['metDoc' + str(rowcount)],header[i],row[i])
        elif normalise.isFieldforActorName(header[i]) == True:
            normalise.ActorNamesNormalise(globals()['metDoc' + str(rowcount)],row[i])

        else:
            #print(row)
            #print('column: ' + str(i) + header[i])

            myfield = normalise.AddValueasXML(globals()['metDoc' + str(rowcount)],header[i],row[i])

        if row[i] == "Katsushika Hokusai":
            normalise.AddExternalURIs(globals()['metDoc' + str(rowcount)],'1820',row[i],"Person","BM")


myxml = ET.tostring(met,pretty_print=True,method='xml',encoding='unicode')
print(myxml,file=w)
