
import csv
import re
from lxml import etree as ET
from bs4 import BeautifulSoup
import langdetect

import pandas

##glossary http://mercury.lcs.mit.edu/~jnc/prints/glossary.html


################  Check against a list of fields for which date normalisation is needed. #########################

def isFieldforDateNormalisation(field):
    datenormaliselist = ['Artist Begin Date','Artist End Date','Object Date','Object Begin Date','Object End Date']
    if field in datenormaliselist:
        return True
    else:
        return False

################  Check against a list for fields for which dimension normalisation is needed.  ####################

def isFieldforDimensionNormalisation(field):
    datenormaliselist = ['Dimensions']
    if field in datenormaliselist:
        return True
    else:
        return False

def isFieldforLanguageNormalisation(field):
    datenormaliselist = ['Title']
    if field in datenormaliselist:
        return True
    else:
        return False



######  Normalise the date and return xml  ##################################

def DateNormalise(one, two, three ):
    return(0)

##########  Normalise the dimension and return xml #################################


def DimensionNormalise(parent, element_header, value):


    m1 = re.search(r'^(?P<prefix>.*?)(?P<heightin>\d.*?)(x)(?P<widthin>.*?)(?P<inches>in).*?(?P<openb>\()(?P<heightcm>.*?)(x)(?P<widthcm>.*?)(?P<centimeters>cm)(?P<closeB>\))$',\
                   value.strip())






    if m1:

        element_header = element_header.replace(" ", "_")
        dimensions = ET.SubElement(parent, str(element_header)) # an element to include all dimensions

        dimension1 =  ET.SubElement(dimensions, 'dimension')    #element for first doimension set
        heightin = ET.SubElement(dimension1,'value')            #the dimnension value
        heightin.text = m1.group('heightin')
        type = ET.SubElement(dimension1, 'type')                #the dimension type
        type.text = 'height'                                      #height
        unit = ET.SubElement(dimension1, 'unit')                #the dimension unit
        unit.text = 'inches'                          #inches

        dimension2 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
        widthin = ET.SubElement(dimension2,'value')
        widthin.text = m1.group('widthin')
        type = ET.SubElement(dimension2, 'type')  # the dimension type
        type.text = 'width'  # height
        unit = ET.SubElement(dimension2, 'unit')  # the dimension unit
        unit.text = 'inches'  # inches

        dimension3 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
        widthin = ET.SubElement(dimension3, 'value')
        widthin.text = m1.group('heightcm')
        type = ET.SubElement(dimension3, 'type')  # the dimension type
        type.text = 'height'  # height
        unit = ET.SubElement(dimension3, 'unit')  # the dimension unit
        unit.text = 'centimeters'  # inches

        dimension4 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
        widthin = ET.SubElement(dimension4,'value')
        widthin.text = m1.group('widthcm')
        type = ET.SubElement(dimension4, 'type')  # the dimension type
        type.text = 'width'  # height
        unit = ET.SubElement(dimension4, 'unit')  # the dimension unit
        unit.text = 'centimeters'  # inches

        return()
    else:
        return()

def LanguageNormalise(parent, element_header, value, delimiter):
    field = element_header.replace(" ", "_")
    multilang = value.split('|')

    for i in range(0,len(multilang)):
        globals()[field + str(i)] = ET.SubElement(parent, field)
        text = ET.SubElement(globals()[field + str(i)], 'text')
        text.text = multilang[i]
        if len(multilang[i]) > 0:
            text = ET.SubElement(globals()[field + str(i)], 'lang')
            text.text = str(langdetect.detect(multilang[i]))
    return()


def AddValueasXML(parent, element_header, value):
    print(element_header,value)
    element_header = element_header.replace(" ","_")
    field = ET.SubElement(parent,str(element_header))
    field.text = value
    return field

######   This opens and clears the file for appending  ###############
f = open('HokusaiMetObjects.csv','r',encoding='utf8')
w = open('hok.xml','w',encoding='utf8')
w.close()
w = open('hok.xml','a',encoding='utf8')

#########    This reads as CSV    #######################################

myreader = csv.reader(f,delimiter=',')


############    This initiates an XML document for writing in the new elements from the CSV ####################

metDoc = ET.Element("metobject")

#############   This gets the first row which contans the header (firld names) ###########################

header = next(myreader)

#############   This gets the number of fields ###########################################

columns = len(header)

for row in myreader:
    for i in range(0,columns):
        if isFieldforDateNormalisation(header[i]) == True:
            print(header[i], row[i])
            DateNormalise(metDoc, header[i],row[i])
        elif isFieldforDimensionNormalisation(header[i]) == True:
            print(header[i], row[i])
            DimensionNormalise(metDoc, header[i],row[i])
        elif isFieldforLanguageNormalisation(header[i]) == True:
            print(header[i], row[i])
            LanguageNormalise(metDoc, header[i],row[i],'|')
        else:
            myfield = AddValueasXML(metDoc,header[i],row[i])




myxml = ET.tostring(metDoc,pretty_print=True,method='xml',encoding='unicode')
print(BeautifulSoup(myxml, "xml").prettify(),file=w)