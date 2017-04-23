
import csv
import re
from lxml import etree as ET
from bs4 import BeautifulSoup
import langdetect
import nltk
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

###############################  Seperation of fields with delimited language versions  ####################


def isFieldforLanguageNormalisation(field):
    datenormaliselist = ['Title']
    if field in datenormaliselist:
        return True
    else:
        return False




#####################################  Normalise the date and return xml  ##################################

def DateNormalise(parent, element_header, value):
    m1 = re.search(r'^(?P<date>\d{4}$)',value.strip())
    m2 = re.search(r'^(?P<prefix>\w.+?)(?P<date>\d{4}$)',value.strip())


    if m1:
        value = value.strip()
        element_header = element_header.replace(" ", "_")
        if 'Begin' in element_header and 'Object' in element_header:
            object_dates = ET.SubElement(parent, "object_date")
            begin = ET.SubElement(object_dates, element_header)
            begin.text = m1.group('date').strip() +'-01-01'
        if 'End' in element_header and 'Object' in element_header:
            object_dates = ET.SubElement(parent, "object_date")
            begin = ET.SubElement(object_dates, element_header)
            begin.text = m1.group('date').strip() + '-12-31'
        if 'Begin' in element_header and 'Artist' in element_header:
            artist_dates = ET.SubElement(parent, "artist_date")
            begin = ET.SubElement(artist_dates, element_header)
            begin.text = m1.group('date').strip() + '-01-01'
        if 'End' in element_header and 'Artist' in element_header:
            artist_dates = ET.SubElement(parent, "artist_date")
            begin = ET.SubElement(artist_dates, element_header)
            begin.text = m1.group('date').strip() + '-12-31'

        print('m1 - hit: ' + value)
    elif m2:
        value = value.strip()
        element_header = element_header.replace(" ", "_")
        if 'Begin' in element_header and 'Object' in element_header:
            object_dates = ET.SubElement(parent, "object_date")
            begin = ET.SubElement(object_dates, element_header)
            begin.text = m2.group('date').strip() + '-01-01'
        if 'End' in element_header and 'Object' in element_header:
            object_dates = ET.SubElement(parent, "object_date")
            begin = ET.SubElement(object_dates, element_header)
            begin.text = m2.group('date').strip() + '-12-31'
        if 'Begin' in element_header and 'Artist' in element_header:
            artist_dates = ET.SubElement(parent, "artist_date")
            begin = ET.SubElement(artist_dates, element_header)
            begin.text = m2.group('date').strip() + '-01-01'
        if 'End' in element_header and 'Artist' in element_header:
            artist_dates = ET.SubElement(parent, "artist_date")
            begin = ET.SubElement(artist_dates, element_header)
            begin.text = m2.group('date').strip() + '-12-31'

        print('m2 - hit: ' + value)
    else:
        print('m1 - miss: ' + value)


def Create Dimensions



##########  Normalise the dimension and return xml #################################


def DimensionNormalise(parent, element_header, value):

    global count
    heightinches = ''
    heightcentimeters = ''
    widthinches = ''
    widthcentimeters = ''


    m1 = re.search(r'^(?P<prefix>.*?)(?P<heightin>\d.*?)(x)(?P<widthin>.*?)(?P<inches>in).*?(?P<openb>\()(?P<heightcm>.*?)(x)(?P<widthcm>.*?)(?P<centimeters>cm)(?P<closeB>\))$',\
                   value.strip())

    m2 = re.search(r'^(?P<heightlabel>.+?)\.(?P<heighin>.+?) .+\((?P<heighcm>.+?)cm.+?(?P<widthlabel>.+?)\.(?P<widthin>.+?)in\..+?\((?P<widthcm>.+?)cm.*$',value.strip())

    m3 = re.search(r'^(?P<heightin>\d.*?)x|×(?P<widthin>.+?)in.+?\((?P<heightcm>.+?)x|×(?P<widthcm>.+?)cm\)$',value.strip())

    m4 = re.search(r'^.+?(?P<heightin>\d.*?)x|×(?P<widthin>.+?)in.+?\((?P<heightcm>.+?)x|×(?P<widthcm>.+?)cm\)$',value.strip())

    m5 = re.search(r'^H\..+?(?P<heightin>\d.*?)in.+?\((?P<heightcm>.+?)cm.+?W.(?P<widthin>.+?)in.+?\((?P<widthcm>.+?)cm\)$',value.strip())



    CreateDimensions()


    if m1:
        heightinches = m1.group('heightin').strip()
        heightcentimeters = m1.group('heightcm').strip()
        widthinches = m1.group('widthin').strip()
        widthcentimeters = m1.group('widthcm').strip()
        CreateDimensions()










        element_header = element_header.replace(" ", "_")
        dimensions = ET.SubElement(parent, str(element_header))  # an element to include all dimensions

        dimension1 =  ET.SubElement(dimensions, 'dimension')     #element for first doimension set
        heightin = ET.SubElement(dimension1,'value')             #the dimnension value
        heightin.text = m1.group('heightin').strip()
        type = ET.SubElement(dimension1, 'type')                 #the dimension type
        type.text = 'height'                                     #height
        unit = ET.SubElement(dimension1, 'unit')                 #the dimension unit
        unit.text = 'inches'                                     #inches

        dimension2 = ET.SubElement(dimensions, 'dimension')      # element for second dimension set
        widthin = ET.SubElement(dimension2,'value')
        widthin.text = m1.group('widthin').strip()
        type = ET.SubElement(dimension2, 'type')                 # the dimension type
        type.text = 'width'                                      # height
        unit = ET.SubElement(dimension2, 'unit')                 # the dimension unit
        unit.text = 'inches'                                     # inches

        dimension3 = ET.SubElement(dimensions, 'dimension')      # element for second dimension set
        widthin = ET.SubElement(dimension3, 'value')
        widthin.text = m1.group('heightcm').strip()
        type = ET.SubElement(dimension3, 'type')                 # the dimension type
        type.text = 'height'                                     # height
        unit = ET.SubElement(dimension3, 'unit')                 # the dimension unit
        unit.text = 'centimeters'                                # centimeters

        dimension4 = ET.SubElement(dimensions, 'dimension')      # element for second dimension set
        widthin = ET.SubElement(dimension4,'value')
        widthin.text = m1.group('widthcm').strip()
        type = ET.SubElement(dimension4, 'type')                 # the dimension type
        type.text = 'width'                                      # height
        unit = ET.SubElement(dimension4, 'unit')                 # the dimension unit
        unit.text = 'centimeters'                                # centimeters

        #print('m1 - hit: ' + value)
        count += 1

    elif m2:

        #print('m2 - hit: ' + value)
        count += 1

    elif m3:

        #print('m3 - hit: ' + value)
        count += 1

    elif m4:

        #print('m4 - hit: ' + value)
        count += 1

    elif m5:

        #print('m5 - hit: ' + value)
        count += 1

    else:
        #print('miss: ' + value)
        count += 1

#########################LanguageNormalise - take some text and determine the unicode language code####

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


#########################LanguageNormalise - take some text and determine the unicode language code#### 

def AddExternalURIs(parent,id,label,type,org):
    link = ET.SubElement(parent, 'link')
    sublink = ET.SubElement(link, 'type')
    sublink.text = type
    subid = ET.SubElement(link, 'id')
    subid.text = id
    subid = ET.SubElement(link, 'organisation')
    subid.text = org

    return()


def AddValueasXML(parent, element_header, value):
    #print(element_header,value)
    element_header = element_header.replace(" ","_")
    field = ET.SubElement(parent,str(element_header))
    field.text = value
    return field

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
    for i in range(0,columns):
        if isFieldforDateNormalisation(header[i]) == True:
            #print(header[i], row[i])
            DateNormalise(metDoc, header[i],row[i])
        elif isFieldforDimensionNormalisation(header[i]) == True:
            #print(header[i], row[i])
            DimensionNormalise(metDoc, header[i],row[i])
        elif isFieldforLanguageNormalisation(header[i]) == True:
            #print(header[i], row[i])
            LanguageNormalise(metDoc, header[i],row[i],'|')
        else:
            myfield = AddValueasXML(metDoc,header[i],row[i])

        if row[i] == "Katsushika Hokusai":
            AddExternalURIs(metDoc,'1820',row[i],"Person","BM")

print(count)
print(rowcount)
myxml = ET.tostring(metDoc,pretty_print=True,method='xml',encoding='unicode')
print(BeautifulSoup(myxml, "xml").prettify(),file=w)