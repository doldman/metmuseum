from lxml import etree as ET
import re
import langdetect

################  Check against a list of fields for which date normalisation is needed. #########################

def isFieldforDateNormalisation(field):
    datenormaliselist = ['Artist Begin Date','Artist End Date','Object Begin Date','Object End Date']
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




    else:
        print('miss: ' + element_header + ' ' + value)


def CreateDimensions(dvalue,dunit,dtype,prefix=''):

    global count

    dimension = ET.Element('dimension')  # element for first doimension set
    value = ET.SubElement(dimension, 'value')  # the dimnension value
    value.text = dvalue.strip()
    type = ET.SubElement(dimension, 'type')  # the dimension type
    type.text = str(prefix) + ' ' + dtype  # height
    unit = ET.SubElement(dimension, 'unit')  # the dimension unit
    unit.text = dunit  # inches

    print(ET.tostring(dimension))

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
        print('m1\n')
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

        print('m2\n')
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

        print('m3\n')
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

        print('m4\n')
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

        print('m4a\n')
        count = str(m4a.re).count('prefix')

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

        print('m5\n')
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

        print('m6\n')
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


    else:
        print('missed dimension: ' + value)



#########################LanguageNormalise - take some text and determine the unicode language code####

def LanguageNormalise(parent, element_header, value, delimiter):

    seriessplit = []

    field = element_header.replace(" ", "_")
    if value.find(delimiter)>0:
        #splitOnLanguage = value.split(delimiter)


        multilang = value.split(delimiter)        #split the field into two titles

        if str(langdetect.detect(multilang[1])) == 'en' and multilang[1].find('from the series'):
            seriessplit = multilang[1].split('from the series')
            multilang[1] = seriessplit[0]

        for i in range(0,len(multilang)):
            globals()[field + str(i)] = ET.SubElement(parent, field)
            text = ET.SubElement(globals()[field + str(i)], 'text')
            text.text = multilang[i]
            if len(multilang[i]) > 0:
                text = ET.SubElement(globals()[field + str(i)], 'lang')
                text.text = str(langdetect.detect(multilang[i]))


        if len(seriessplit) > 1:
            series = ET.SubElement(parent,'series_title')
            series.text = seriessplit[1]

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