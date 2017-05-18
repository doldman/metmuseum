from lxml import etree as ET
import re
import langdetect
from bs4 import BeautifulSoup
import nltk
import pandas


actorlist = []

################  Check against a list of fields for which date normalisation is needed. #########################

def isFieldforDateNormalisation(field):
    normaliselist = ['Artist Begin Date','Artist End Date','Object Begin Date','Object End Date']
    if field in normaliselist:
        return True
    else:
        return False

def isMedium(field):
    normaliselist = ['Medium']
    if field in normaliselist:
        return True
    else:
        return False

def isFieldforActorName(field):
    normaliselist = ['Artist Display Name']
    if field in normaliselist:
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

#####################################################################################################################

def ConvertAttributestoTags():



    root = ET.XML(r'<main><dimension h="2" w="3">hjhjj</dimension></main>')

    find = ET.XPath('//dimension/@h')

    print(find(root)[0].text)




###############################  Seperation of fields with delimited language versions  ####################


def isFieldforLanguageNormalisation(field):
    datenormaliselist = ['Title']
    if field in datenormaliselist:
        return True
    else:
        return False

###############################  Seperation of fields with delimited language versions  ####################


def isFieldforPeriod(field):
    datenormaliselist = ['Period']
    if field in datenormaliselist:
        return True
    else:
        return False

###############################  tease out Period  ####################

def PeriodNormalise(parent,element,value):
    m1 = re.search(r'(?P<period>^\w+).+?(?P<word>\w+).+?\((?P<range>.*)\)$',value.strip())

    if m1:
        element = element.replace(" ", "_")
        period = ET.SubElement(parent,"Period")
        period.text = m1.group('period').strip()
        #print('hit ' + m1.group('period'))
    else:
        period = ET.SubElement(parent, "Period")
        period.text = ''
        #print('miss- period ' + value)


######################### Technique and Material ##########################################################

def typetechniqueNormalise(parent, element, value):


    if value.find(';') > -1:
        parts = value.split(';')

        tech = ET.SubElement(parent, "Technique")
        tech.text = parts[0].strip()

        tokens = nltk.word_tokenize(parts[1])
        tagged = nltk.pos_tag(tokens)

        technote = ET.SubElement(parent,'Technique_Note')
        technote.text = parts[1].strip()

        i = 1
        for tag in tagged:
            if tag[1] == 'NN':
                globals()['material' + str(i)] = ET.SubElement(parent,'Material')
                globals()['material' + str(i)].text = tag[0]
                i += 1

    else:
        tech = ET.SubElement(parent, "Object_Type")
        tech.text = value.strip()





#####################################  Normalise the date and return xml  ##################################

def DateNormalise(parent, element_header, value):
    m1 = re.search(r'^(?P<date>\d{4}$)',value.strip())
    m2 = re.search(r'^(?P<prefix>\w.+?)(?P<date>\d{4}$)',value.strip())
    m3 = re.search(r'(?P<century1>^\d\d)th.+?(?P<century2>\d\d)th.+?$',value.strip())




    if m1:
        #print('m1\n')
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

        #print('m1 - hit: ' + value)
    elif m2:
        #print('m2\n')
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

        #print('m2 - hit: ' + value)

    elif m3:
         element_header = element_header.replace(" ", "_")




    #else:
        #print('miss: ' + element_header + ' ' + value)


def CreateDimensions(dvalue,dunit,dtype,prefix=''):

    global count

    dimension = ET.Element('dimension')  # element for first doimension set
    value = ET.SubElement(dimension, 'value')  # the dimnension value
    value.text = dvalue.strip()
    type = ET.SubElement(dimension, 'type')  # the dimension type
    type.text = str(prefix) + ' ' + dtype  # height
    unit = ET.SubElement(dimension, 'unit')  # the dimension unit
    unit.text = dunit  # inches

    #print(ET.tostring(dimension))

    return(dimension)


    # dimension2 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
    # widthin = ET.SubElement(dimension2, 'value')
    # widthin.text = widthIn.strip()
    # type = ET.SubElement(dimension2, 'type')  # the dimension type
    # type.text = 'width'  # height
    # unit = ET.SubElement(dimension2, 'unit')  # the dimension unit
    # unit.text = 'inches'  # inches
    #
    # dimension3 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
    # widthin = ET.SubElement(dimension3, 'value')
    # widthin.text = heightCm.strip()
    # type = ET.SubElement(dimension3, 'type')  # the dimension type
    # type.text = 'height'  # height
    # unit = ET.SubElement(dimension3, 'unit')  # the dimension unit
    # unit.text = 'centimeters'  # centimeters
    #
    # dimension4 = ET.SubElement(dimensions, 'dimension')  # element for second dimension set
    # widthin = ET.SubElement(dimension4, 'value')
    # widthin.text = widthCm.strip()
    # type = ET.SubElement(dimension4, 'type')  # the dimension type
    # type.text = 'width'  # height
    # unit = ET.SubElement(dimension4, 'unit')  # the dimension unit
    # unit.text = 'centimeters'  # centimeters
    #
    # # print('m1 - hit: ' + value)
    # count += 1



##########  Normalise the dimension and return xml #################################


def DimensionNormalise(parent, element_header, value):

    value = value.replace('\n','')

    chars = len(value)

    heightinches = ''
    heightcentimeters = ''
    widthinches = ''
    widthcentimeters = ''

    fieldname = element_header.replace(" ", "_")
    dimensions = ET.Element(str(fieldname))  # an element to include all dimensions


    m1 = re.search(r'^(?P<prefix>.*?):.+?(?P<heightin>\d.*?)x(?P<widthin>.*?)in.*?\((?P<heightcm>.*?)x(?P<widthcm>.*?)cm\)$',value.strip())

    m2 = re.search(r'^(?P<heightlabel>.+?)\.(?P<heightin>.+?) .+\((?P<heightcm>.+?)cm.+?(?P<widthlabel>.+?)\.(?P<widthin>.+?)in\..+?\((?P<widthcm>.+?)cm.*$',value.strip())

    m3 = re.search(r'^(?P<heightin>\d.*?)(x|×)(?P<widthin>.+?)in.+?\((?P<heightcm>.+?)(x|×)(?P<widthcm>.+?)cm\)$',value.strip())

    m4 = re.search(r'(?P<prefix>^\w.+?)(?P<heightin>\d.*?)(x|×)(?P<widthin>.+?)in.+?\((?P<heightcm>.+?)(x|×)(?P<widthcm>.+?)cm\)$',value.strip())

    m4a = re.search(r'(?P<prefix1>^\w.+?)(?P<heightin1>\d.*?)(x|×)(?P<widthin1>.+?)in.+?\((?P<heightcm1>.+?)(x|×)(?P<widthcm1>.+?)cm\)(?P<prefix2>.+?):.+?(?P<heightin2>\d.*?)(x|×)(?P<widthin2>.+?)in.+?\((?P<heightcm2>.+?)(x|×)(?P<widthcm2>.+?)cm\)$',value.strip())

    m5 = re.search(r'^H\..+?(?P<heightin>\d.*?)in.+?\((?P<heightcm>.+?)cm.+?W.(?P<widthin>.+?)in.+?\((?P<widthcm>.+?)cm\)$',value.strip())

    m6 = re.search(r'(?P<prefix1>^.+?):.+?(?P<heightin1>\d.*?)(x|×)(?P<widthin1>.+?)in.+?\((?P<heightcm1>.+?)(x|×)(?P<widthcm1>.+?)(cm)\)(?P<prefix2>\w.+?):.+?(?P<heightin2>\d.+?)(x|×).+?(?P<widthin2>\d.+?)in.+?\((?P<heightcm2>.+?)(x|×)(?P<widthcm2>.+?)cm\)(?P<prefix3>\w.+?):.+?(?P<heightin3>.+?)(x|×).+?(?P<widthin3>.+?)in.+?\((?P<heightcm3>.+?)(x|×).+?(?P<widthcm3>.+?)cm\)$',value.strip())


    if m1 and not m6:
        #print('m1\n')
        heightinches = m1.group('heightin').strip()
        heightcentimeters = m1.group('heightcm').strip()
        widthinches = m1.group('widthin').strip()
        widthcentimeters = m1.group('widthcm').strip()
        HI = CreateDimensions(heightinches, 'inches', 'height')
        dimensions.append(HI)
        HC = CreateDimensions(heightcentimeters, 'centimeters', 'height')
        dimensions.append(HC)
        WI = CreateDimensions(widthinches, 'inches', 'width')
        dimensions.append(WI)
        WC = CreateDimensions(widthcentimeters, 'centimeters', 'width')
        dimensions.append(WC)
        parent.append(dimensions)

        return dimensions

    elif m2 and not m6:

        #print('m2\n')
        heightinches = m2.group('heightin').strip()
        heightcentimeters = m2.group('heightcm').strip()
        widthinches = m2.group('widthin').strip()
        widthcentimeters = m2.group('widthcm').strip()
        HI = CreateDimensions(heightinches,'inches','height')
        dimensions.append(HI)
        HC = CreateDimensions(heightcentimeters,'centimeters','height')
        dimensions.append(HC)
        WI = CreateDimensions(widthinches,'inches','width')
        dimensions.append(WI)
        WC = CreateDimensions(widthcentimeters, 'centimeters','width')
        dimensions.append(WC)
        parent.append(dimensions)

        return dimensions

    elif m3 and not m6:

        #print('m3\n')
        heightinches = m3.group('heightin').strip()
        heightcentimeters = m3.group('heightcm').strip()
        widthinches = m3.group('widthin').strip()
        widthcentimeters = m3.group('widthcm').strip()
        HI = CreateDimensions(heightinches,'inches','height')
        dimensions.append(HI)
        HC = CreateDimensions(heightcentimeters,'centimeters','height')
        dimensions.append(HC)
        WI = CreateDimensions(widthinches,'inches','width')
        dimensions.append(WI)
        WC = CreateDimensions(widthcentimeters, 'centimeters','width')
        dimensions.append(WC)
        parent.append(dimensions)

        return dimensions

    elif m4 and not m6 and not m4a:

        #print('m4\n')
        heightinches = m4.group('heightin').strip()
        heightcentimeters = m4.group('heightcm').strip()
        widthinches = m4.group('widthin').strip()
        widthcentimeters = m4.group('widthcm').strip()
        HI = CreateDimensions(heightinches,'inches','height')
        dimensions.append(HI)
        HC = CreateDimensions(heightcentimeters,'centimeters','height')
        dimensions.append(HC)
        WI = CreateDimensions(widthinches,'inches','width')
        dimensions.append(WI)
        WC = CreateDimensions(widthcentimeters, 'centimeters','width')
        dimensions.append(WC)
        parent.append(dimensions)

        return dimensions

    elif m4a and not m6 :

        #print('m4a\n')
        count = 0
        for key in m4a.re.groupindex.keys():
            if 'prefix' in str(key):
                count = count + 1

        for i in range(1, count + 1):

            prefix = m4a.group('prefix' + str(i)).strip()
            heightinches = m4a.group('heightin' + str(i)).strip()
            heightcentimeters = m4a.group('heightcm' + str(i)).strip()
            widthinches = m4a.group('widthin' + str(i)).strip()
            widthcentimeters = m4a.group('widthcm' + str(i)).strip()
            HI = CreateDimensions(heightinches, 'inches', 'height', prefix)
            dimensions.append(HI)
            HC = CreateDimensions(heightcentimeters, 'centimeters', 'height', prefix)
            dimensions.append(HC)
            WI = CreateDimensions(widthinches, 'inches', 'width', prefix)
            dimensions.append(WI)
            WC = CreateDimensions(widthcentimeters, 'centimeters', 'width', prefix)
            dimensions.append(WC)
            parent.append(dimensions)

        return dimensions


    elif m5 and not m6:

        #print('m5\n')
        heightinches = m5.group('heightin').strip()
        heightcentimeters = m5.group('heightcm').strip()
        widthinches = m5.group('widthin').strip()
        widthcentimeters = m5.group('widthcm').strip()
        HI = CreateDimensions(heightinches,'inches','height')
        dimensions.append(HI)
        HC = CreateDimensions(heightcentimeters,'centimeters','height')
        dimensions.append(HC)
        WI = CreateDimensions(widthinches,'inches','width')
        dimensions.append(WI)
        WC = CreateDimensions(widthcentimeters, 'centimeters','width')
        dimensions.append(WC)
        parent.append(dimensions)

        return dimensions

    elif m6:

        #print('m6\n')
        #count = str(m6.re).count('prefix')
        count = 0
        for key in m6.re.groupindex.keys():
            if 'prefix' in str(key):
                count = count + 1


        for i in range(1,count + 1):


            prefix = m6.group('prefix' + str(i)).strip()
            heightinches = m6.group('heightin' + str(i)).strip()
            heightcentimeters = m6.group('heightcm'  + str(i)).strip()
            widthinches = m6.group('widthin' + str(i)).strip()
            widthcentimeters = m6.group('widthcm' + str(i)).strip()
            HI = CreateDimensions(heightinches, 'inches', 'height',prefix)
            dimensions.append(HI)
            HC = CreateDimensions(heightcentimeters, 'centimeters', 'height',prefix)
            dimensions.append(HC)
            WI = CreateDimensions(widthinches, 'inches', 'width',prefix)
            dimensions.append(WI)
            WC = CreateDimensions(widthcentimeters, 'centimeters', 'width',prefix)
            dimensions.append(WC)
            parent.append(dimensions)

        return dimensions


            # prefix = m6.group('prefix2').strip()
        # heightinches = m6.group('heightin2').strip()
        # heightcentimeters = m6.group('heightcm2').strip()
        # widthinches = m6.group('widthin2').strip()
        # widthcentimeters = m6.group('widthcm2').strip()
        #
        # CreateDimensions(heightinches, heightcentimeters, widthinches, widthcentimeters, fieldname, parent)
        #
        # prefix = m6.group('prefix3').strip()
        # heightinches = m6.group('heightin3').strip()
        # heightcentimeters = m6.group('heightcm3').strip()
        # widthinches = m6.group('widthin3').strip()
        # widthcentimeters = m6.group('widthcm3').strip()
        #
        # CreateDimensions(heightinches, heightcentimeters, widthinches, widthcentimeters, fieldname, parent, prefix)
        #


    #else:
       # print('missed dimension: ' + value)



#########################LanguageNormalise - take some text and determine the unicode language code####

def ProcessJapanese(parent, header, titles):

    splittitle = []
    if titles.find(u'\u3000') > -1:
        splittitle = titles.rsplit('\u3000',1)
        jptitles = ET.SubElement(parent,'Titles')
        jptitle = ET.SubElement(jptitles,'title')
        jptitle.text = splittitle[1]
        jplanguage = ET.SubElement(jptitles,'Language')
        jplanguage.text = 'ja'

        jpseries = ET.SubElement(parent,'Titles')
        jpserial = ET.SubElement(jpseries,'serial')
        jpserial.text = splittitle[0]
        jplanguage = ET.SubElement(jpseries, 'Language')
        jplanguage.text = 'ja'

    else:
        splittitle.append(titles)
        jptitles = ET.SubElement(parent, 'Titles')
        jptitle = ET.SubElement(jptitles, 'title')
        jptitle.text = splittitle[0]
        jplanguage = ET.SubElement(jptitles, 'Language')
        jplanguage.text = 'ja'


def ProcessTitle(parent, title, language, type):

    engtitles = ET.SubElement(parent, 'Titles')
    engtitle = ET.SubElement(engtitles,type)
    engtitle.text = title
    titlelang = ET.SubElement(engtitles, 'Language')
    titlelang.text = language
    #print(title + " : " + language + " : " + type)


def ProcessTitleStrings(parent, element_header, value, delimiter):

    value = value.replace(',','')
    langsplit = []
    seriessplit = []
    field = element_header.replace(" ", "_")
    if value.find(delimiter) > -1:
        langsplit = value.split('|')
        japanesetitles = langsplit[0]
        englishtitles = langsplit[1]
        ProcessJapanese(parent,element_header, japanesetitles) #this is the first japanese split taking title and series title



        if englishtitles.find('from the series') > -1:
            seriessplit = englishtitles.split('from the series')
            engtitles = seriessplit[0]
            engseries = seriessplit[1]


            if engtitles.find('(') > -1:
                startRoman = engtitles.find('(')
                endRoman = engtitles.find(')')
                engTitle = engtitles[0:startRoman]
                romanTitle = engtitles[startRoman+1:endRoman]
                additionaltext = engtitles[endRoman + 1:]
                ProcessTitle(parent,engTitle + " " + additionaltext,'en','title')
                ProcessTitle(parent, romanTitle,'ja-Latn','title')

            else:
                ProcessTitle(parent,engtitles,'en','title')

            if engseries.find('(') > -1:
                startRoman = engseries.find('(')
                endRoman = engseries.find(')')
                engSerial = engseries[0:startRoman]
                romanSerial = engseries[startRoman+1:endRoman]
                ProcessTitle(parent,engSerial,'en','serial')
                ProcessTitle(parent, romanSerial,'ja-Latn','serial')

            else:
                ProcessTitle(parent, engseries,'en','serial')

        else:
                if englishtitles.find('(') > -1:
                    startRoman = englishtitles.find('(')
                    endRoman = englishtitles.find(')')
                    engTitle = englishtitles[0:startRoman]
                    romanTitle = englishtitles[startRoman+1:endRoman]
                    ProcessTitle(parent, engTitle,'en','title')
                    ProcessTitle(parent, romanTitle, 'ja-Latn', 'title')
                else:
                    ProcessTitle(parent, englishtitles, 'en', 'title')
    else:

        if value.find('(') > -1:
            startRoman = value.find('(')
            endRoman = value.find(')')
            myTitle = englishtitles[0 - startRoman]
            myromanTitle = englishtitles[startRoman - endRoman]
            ProcessTitle(parent, engTitle, 'en', 'title')
            ProcessTitle(parent, romanTitle, 'ja-Latn', 'title')

        else:
            if langdetect.detect(value) == 'ja':
                ProcessTitle(parent, value, 'ja', 'Title')
            else:
                ProcessTitle(parent, value, 'en', 'Title')


    return()


def ActorAttributesNormalise(parent,actor):

    myActors = ET.SubElement(parent, 'Actors')

    i = 0
    for item in actor:
        if item.find('|') > -1:
            field = item.split('|')
            items = len[field]

            for i in range(items - 1):
                globals()['p'+ i][i] = field[i]




        else:

            actor = ET.SubElement(myActors,'Actor')
            role = ET.SubElement(actor, 'role')
            role.text = item
            prefix = ET.SubElement(actor, 'prefix')
            prefix.text = item
            name = ET.SubElement(actor, 'name')
            name.text = item
            bio = ET.SubElement(actor, 'bio')
            bio.text = item

            # for person in myactors:
    #
    #     myActor = ET.SubElement(myActors, 'Actor')
    #     myActor.text = person


def ActorNamesNormalise(parent,actor):

    people = []

    if actor.find('|') > -1:
        people = actor.split('|')
    else:
        people.append(actor)


    myActors = ET.SubElement(parent, 'Actors')
    for person in people:
        myActor = ET.SubElement(myActors, 'Actor')
        myActor.text = person
        #if actor == 'Katsushika Hokusai':
        #    myBMlink = ET.SubElement(myActors,'britishmuseumid')
        #    myBMlink.text = '1820'

        if person not in actorlist:
                actorlist.append(person)




    #myxml = ET.tostring(myActors, pretty_print=True, method='xml', encoding='unicode')
    #print(myxml)







        # seriessplit = langsplit[1].split('from the series')
        # ProcessEnglishTitles()
        # ProcessEnglishSeries()


def LanguageNormalise(parent, element_header, value, delimiter):

     ProcessTitleStrings(parent,element_header,value,delimiter)





#########################LanguageNormalise - take some text and determine the unicode language code####



def AddValueasXML(parent, element_header, value):
    #print(element_header,value)
    element_header = element_header.replace(" ","_")
    field = ET.SubElement(parent,str(element_header))
    field.text = value
    return field
