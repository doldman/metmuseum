#met museum csv


import csv
import re
from lxml import etree as ET
from bs4 import BeautifulSoup


f = open('HokusaiMetObjects.csv','r',encoding='utf8')
w = open('newmetsample.xml','w',encoding='utf8')
w.close()
w = open('newmetsample.xml','a',encoding='utf8')



myreader = csv.reader(f,delimiter=',')
print(r'<?xml version="1.0" encoding="UTF-8"?>',end="\n",file=w)
print('<metmuseum>',end="\n",file=w)
for row in myreader:

    if row[0] != "﻿Object Number":


        print('<metobject>',end="\n",file=w)
        print('\t<object_no>'+row[0].strip()+'</object_no>',end="\n",file=w)
        print('\t<IsHighlight>'+row[1].strip()+'</IsHighlight>',end="\n",file=w)
        print('\t<IsPublicDomain>'+row[2] +'</IsPublicDomain>',end="\n",file=w)
        print('\t<ObjectID>'+row[3].strip()+'</ObjectID>',end="\n",file=w)
        print('\t<Department>'+row[4].strip()+'</Department>',end="\n",file=w)
        print('\t<ObjectName>'+row[5].strip()+'</ObjectName>',end="\n",file=w)

        # print('<metobject>',end="\n",file=w)
        # print('\t<object_no>'+row[0].strip()+'</object_no>',end="\n",file=w)
        # print('\t<IsHighlight>'+row[1].strip()+'</IsHighlight>',end="\n",file=w)
        # print('\t<IsPublicDomain>'+row[2].strip() +'</IsPublicDomain>',end="\n",file=w)
        # print('\t<ObjectID>'+row[3].strip()+'</ObjectID>',end="\n",file=w)
        # print('\t<Department>'+row[4].strip()+'</Department>',end="\n",file=w)
        # print('\t<ObjectName>'+row[5].strip()+'</ObjectName>',end="\n",file=w)

        myfirstsection = '<metobject>\n\t<object_no>'+row[0].strip()+'</object_no>\n\t<IsHighlight>'+row[1].strip()+'</IsHighlight>\n\t<IsPublicDomain>'+row[2].strip()+'</IsPublicDomain>\n\t<ObjectID>'+row[3].strip()+'</ObjectID>\n\t<Department>'+row[4].strip()+'</Department>\n\t<ObjectName>'+row[5].strip()+'</ObjectName>\n'



        mytitle = row[6].strip()
        if '|' in mytitle:
            mytitles = mytitle.split('|')
            print('\t<Title>' + mytitles[0].strip() + '</Title>', end="\n", file=w)
            print('\t<Title>' + mytitles[1].strip() + '</Title>', end="\n", file=w)
            mytitlesection = '\t<Title>' + mytitles[0].strip() + '</Title>\n\t<Title>' + mytitles[1].strip() + '</Title>\n'
        else:
            print('\t<Title>'+row[6].strip()+'</Title>',end="\n",file=w)
            mytitlesection = '\t<Title>'+row[6].strip()+'</Title>\n'

        print('\t<Culture>'+row[7].strip()+'</Culture>',end="\n",file=w)
        print('\t<Period>'+row[8].strip()+'</Period>',end="\n",file=w)
        print('\t<Dynasty>'+row[9].strip()+'</Dynasty>',end="\n",file=w)
        print('\t<Reign>'+row[10].strip()+'</Reign>',end="\n",file=w)
        print('\t<Portfolio>'+row[11].strip()+'</Portfolio>',end="\n",file=w)

        mysecondsection = '\t<Culture>'+row[7].strip()+'</Culture>\n\t<Period>'+row[8].strip()+'</Period>\n\t<Dynasty>'+row[9].strip()+'</Dynasty>\n\t<Portfolio>'+row[11].strip()+'</Portfolio>\n'

        myartistrole = row[12].strip()
        myartistassociation = row[13].strip()
        myartistdisplayname = row[14].strip()
        myartistdisplaybio = row[15].strip()
        myartistnationality = row[18].strip()
        myartistbegin = row[19].strip()
        myartistend = row[20].strip()


        if '|' in myartistrole: #or '|' in myartistassociation or '|' in myartistdisplayname or '|' in myartistdisplaybio or '|' in myartistnationality or '|' in myartistbegin or '|' in myartistend:
            artistroles = myartistrole.split('|')
            artistassociations = myartistassociation.split('|')
            artistdisplaynames = myartistdisplayname.split('|')
            artistdisplaybios = myartistdisplaybio.split('|')
            artistnationalitys = myartistnationality.split('|')
            artistbegins = myartistbegin.split('|')
            artistends = myartistend.split('|')


            artistno = len(artistroles)

            i = 0

            for i in range(artistno):

                print('\t<artist>', end="\n", file=w)
                print('\t<artistrole>' + artistroles[i].strip() + '</artistrole>', end="\n", file=w)

                artistsection = '\t<artist>\n\t<artistrole>\n'
                if len(artistassociations) >= i + 1:
                    print('\t<artistassociation>' + artistassociations[i].strip() + '</artistassociation>', end="\n",file=w)
                    artistsection = artistsection + '\t<artistassociation>' + artistassociations[i].strip() + '</artistassociation>\n'
                else:
                    print('\t<artistassociation></artistassociation>', end="\n",file=w)
                if len(artistdisplaynames) >= i + 1:
                    print('\t<displayname>' + artistdisplaynames[i].strip() + '</displayname>', end="\n", file=w)
                else:
                    print('\t<displayname></displayname>', end="\n",file=w)
                if len(artistdisplaybios) >= i + 1:
                    print('\t<displaybio>' + artistdisplaybios[i].strip() + '</displaybio>', end="\n", file=w)
                else:
                    print('\t<displaybio></displaybio>', end="\n", file=w)
                if len(artistnationalitys) >= i + 1:
                    print('\t<nationality>' + artistnationalitys[i].strip() + '</nationality>', end="\n", file=w)
                else:
                    print('\t<displaybio></displaybio>', end="\n", file=w)
                if len(artistbegins) >= i + 1:
                    print('\t<artistbegin>' + artistbegins[i].strip() + '</artistbegin>', end="\n", file=w)
                else:
                    print('\t<artistbegin></artistbegin>', end="\n", file=w)
                if len(artistends) >= i + 1:
                    print('\t<artistend>' + artistends[i].strip() + '</artistend>', end="\n", file=w)
                else:
                    print('\t<artistend></artistend>', end="\n", file=w)
                print('\t</artist>', end="\n", file=w)


        else:

            print('\t<artist>', end="\n", file=w)
            print('\t<artistrole>' + row[12].strip() + '</artistrole>', end="\n", file=w)
            print('\t<artistassociation>' + row[13].strip() + '</artistassociation>', end="\n", file=w)
            print('\t<displayname>' + row[14].strip() + '</displayname>', end="\n", file=w)
            print('\t<displaybio>' + row[15].strip() + '</displaybio>', end="\n", file=w)
            print('\t<nationality>' + row[18].strip() + '</nationality>', end="\n", file=w)
            print('\t<artistbegin>' + row[19].strip() + '</artistbegin>', end="\n", file=w)
            print('\t<artistend>' + row[20].strip() + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)




        print('\t<ObjectDate>'+row[21].strip()+'</ObjectDate>',end="\n",file=w)
        print('\t<ObjectBeginDate>'+row[22].strip()+'</ObjectBeginDate>',end="\n",file=w)
        print('\t<ObjectEndDate>'+row[23].strip()+'</ObjectEndDate>',end="\n",file=w)

        temp = row[24].replace(' or ', ',')
        temp = temp.replace('and ', ',')

        mymateriallist = temp.split(',')

        for item in mymateriallist:
            print('\t<Medium>'+item.strip()+'</Medium>',end="\n",file=w)


        m1 = re.search(r'(Diam). *(\d*\/\d*) *(in). *\((\d*.*\d) *(cm)\)', row[25].strip()) #just diameter
        m2 = re.search(r'^H\.\s.*?([^in]+)(in).\s\(([^cm]+)(cm)\)', row[25].strip())   #just height' but exclude m2b
        m2a = re.search(r'(H)\.\s([^in]+)(in).\s\(([^cm]+)(cm)\);\s*(Diam).\s*([^in]+)(in).\s*\(([^cm]+)(cm)\)', row[25].strip())   #height and diam
        m2b = re.search(r'([^H]+)(H).\s([^in]+)(in).\s\(([^cm]+cm)\)', row[25].strip()) # label with height
        m3 = re.search(r'(^\d.*) x (\d.*) x (\d.*) (in).*\((\d.*) x (\d.*) x (\d.*)(cm)\)', row[25].strip())   # 3 dimensions with no label
        m4 = re.search(r'(\w*):\s([^x]+)\sx\s([^x]+)x\s([^in]+)(in).\s\(([^x]+)x\s([^x]+)x\s([^cm]+)(cm)\);\s([^oz]+)(oz).\s([^dwt]+)(dwt).\s\(([^g]+)\s(g)\)', row[25].strip())  #label with 3 dim
        m4a = re.search(r'(\w*):\s([^x]+)\sx\s([^in]+)(in).\s\(([^x]+)x\s([^cm]+)(cm)\);\s([^oz]+)(oz).\s([^dwt]+)(dwt).\s\(([^g]+)\s(g)\)',row[25].strip()) #label with 2 dim
        m5 = re.search(r'(;)([^\:]+):\s(H)\.\s([^in]+)(in).\s\(([^cm]+)(cm)\)', row[25].strip())
        m6 = re.search(r'^(?P<heightin>.*?)(x)(?P<widthin>.*?)(in).*?\((?P<heightcm>.*?)(x)(?P<widthcm>.*?)(?P<centimeters>cm)\)$',row[25].strip())



        if m1:  # just diameter

            xnumber = m1.string.count("diameter")
            print('\t<DimensionSet>', end="\n", file=w)

            if m1.group(5).find("cm") > -1:
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Diameter' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m1.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)

            if m1.group(3).find("in") > -1:
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Diameter' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m1.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)

            print('\t</DimensionSet>', end="\n", file=w)

        if m2 and not m2a:   #just height' but exclude m2b

            if len(m2.groups()) == 4:

                print('\t<DimensionSet>', end="\n", file=w)
                if m2.group(4).find("cm") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                if m2.group(2).find("in") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2.group(1).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)
                print('\t</DimensionSet>', end="\n", file=w)


        if m2a:   #height and diam
            if len(m2a.groups()) == 10:

                print('\t<DimensionSet>', end="\n", file=w)
                if m2a.group(3).find("in") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2a.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                if m2a.group(5).find("cm") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2a.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                if m2a.group(8).find("in") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Diameter' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2a.group(9).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                if m2a.group(10).find("cm") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Diameter' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2a.group(10).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                print('\t</DimensionSet>', end="\n", file=w)

        if m2b: # label with height
            if len(m2b.groups()) == 6:




                print('\t<DimensionsFeature>', end="\n", file=w)
                print('\t\t<DimensionsSet>', end="\n", file=w)
                mydimensionsection = '\t<DimensionsFeature>\n\t\t<DimensionsSet>\n'

                if m2b.group(4).find("in") > -1:


                    print('\t<feature>' + m2b.group(1).strip() + '</feature>', end="\n", file=w)
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2b.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    myxmlsection += '\t<feature>' + m2b.group(
                        1).strip() + '</feature>\n' + '\t\t<Dimension>\n' + '\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>\n' + '\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>' + '\t\t\t<dimensionvalue>' + m2b.group(
                        3).strip() + '</dimensionvalue>\n' + '\t\t</Dimension>\n'
                    print(myxmlsection)

                if m2b.group(6).find("in") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m5.group(5).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    myxmlsection += '\t<feature>' + m2b.group(
                        1).strip() + '</feature>\n' + '\t\t<Dimension>\n' + '\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>\n' + '\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>' + '\t\t\t<dimensionvalue>' + m2b.group(
                        5).strip() + '</dimensionvalue>\n' + '\t\t</Dimension>\n'

                    print(myxmlsection)



                print('\t\t</DimensionsSet>', end="\n", file=w)

                print('\t</DimensionsFeature>', end="\n", file=w)





        if m3:  # 3 dimensions with no label
            if len(m3.groups()) == 8:

                print('\t<DimensionSet>', end="\n", file=w)
                if m3.group(8).find("cm") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(5).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(6).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(7).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                print('\t</DimensionSet>', end="\n", file=w)

                if m3.group(4).find("in") > -1:
                    print('\t<DimensionSet>', end="\n", file=w)

                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(1).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m3.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t</DimensionSet>', end="\n", file=w)




        if m4:  #ovrall example label and 3 dimension

            xnumber = m4.string.count(" x ")
            if len(m4.groups()) == 15 and xnumber == 6:


                print('\t<DimensionsFeature>', end="\n", file=w)

                if m4.group(5).find("in") > -1:
                    print('\t<feature>' + m4.group(1).strip() + '</feature>', end="\n", file=w)
                    print('\t\t<DimensionsSet>', end="\n", file=w)


                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t</DimensionsSet>', end="\n", file=w)

                if m4.group(9).find("cm") > -1:
                    print('\t\t<DimensionsSet>', end="\n", file=w)
                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(6).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(7).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters  ' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(8).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t</DimensionsSet>', end="\n", file=w)

                print('\t</DimensionsFeature>', end="\n", file=w)

        if m4a:  #ovrall example label and 2 dimension

            xnumber = m4a.string.count(" x ")
            if len(m4a.groups()) == 15 and xnumber == 4:


                print('\t<DimensionsFeature>', end="\n", file=w)

                if m4a.group(5).find("in") > -1:
                    print('\t<feature>' + m4a.group(1).strip() + '</feature>', end="\n", file=w)
                    print('\t\t<DimensionsSet>', end="\n", file=w)


                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4a.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4a.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)


                    print('\t\t</DimensionsSet>', end="\n", file=w)

                if m4a.group(9).find("cm") > -1:
                    print('\t\t<DimensionsSet>', end="\n", file=w)
                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4a.group(6).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4a.group(8).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)



                    print('\t\t</DimensionsSet>', end="\n", file=w)

                print('\t</DimensionsFeature>', end="\n", file=w)

        if m5:
            xnumber = m5.string.count(" x ")
            if len(m5.groups()) == 7 and xnumber == 0:
                print(row[25].strip())

        if m6:
            xnumber = m6.string.count(" x ")
            if len(m6.groups()) == 8 and xnumber == 2:
                print()


        print('\t<CreditLine>'+row[26].strip()+'</CreditLine>',end="\n",file=w)




        mygeotype = row[27].strip()
        mycity = row[28].strip()
        mystate = row[29].strip()
        mycounty = row[30].strip()
        mycountry = row[31].strip()
        myregion = row[32].strip()
        mysubregion = row[33].strip()
        mylocale = row[34].strip()
        mylocus = row[35].strip()
        myexcavation = row[36].strip()
        myriver = row[37].strip()



        if '|' in mygeotype:

            geotypes = mygeotype.split('|')
            cities = mycity.split('|')
            states = mystate.split('|')
            counties = mycounty.split('|')
            countries = mycountry.split('|')
            regions = myregion.split('|')
            subregions = mysubregion.split('|')
            locales= mylocale.split('|')
            loci = mylocus.split('|')
            excavations = myexcavation.split('|')
            rivers = myriver.split('|')

            geono = len(geotypes)

            i = 0

            for i in range(geono):

                print('\t<geo>', end="\n", file=w)
                print('\t<geotype>' + geotypes[i].strip() + '</geotype>', end="\n", file=w)
                if len(cities) >= i + 1:
                    print('\t<city>' + cities[i].strip() + '</city>',end="\n", file=w)
                else:
                    print('\t<city></city>', end="\n", file=w)
                if len(states) >= i + 1:
                    print('\t<state>' + states[i].strip() + '</state>', end="\n", file=w)
                else:
                    print('\t<state></state>', end="\n", file=w)

                if len(counties) >= i + 1:
                    print('\t<county>' + counties[i].strip() + '</county>', end="\n", file=w)
                else:
                    print('\t<county></county>', end="\n", file=w)
                if len(countries) >= i + 1:
                    print('\t<county>' + countries[i].strip() + '</county>', end="\n", file=w)
                else:
                    print('\t<county></county>', end="\n", file=w)
                if len(regions) >= i + 1:
                    print('\t<region>' + regions[i].strip() + '</region>', end="\n", file=w)
                else:
                    print('\t<region></region>', end="\n", file=w)
                if len(subregions) >= i + 1:
                    print('\t<subregion>' + subregions[i].strip() + '</subregion>', end="\n", file=w)
                else:
                    print('\t<subregion></subregion>', end="\n", file=w)

                if len(locales) >= i + 1:
                    print('\t<locale>' + locales[i].strip() + '</locale>', end="\n", file=w)
                else:
                    print('\t<locale></locale>', end="\n", file=w)

                if len(loci) >= i + 1:
                    print('\t<locus>' + loci[i].strip() + '</locus>', end="\n", file=w)
                else:
                    print('\t<locus></locus>', end="\n", file=w)

                if len(excavations) >= i + 1:
                    print('\t<excavation>' + excavations[i].strip() + '</excavation>', end="\n", file=w)
                else:
                    print('\t<excavation></excavation>', end="\n", file=w)

                if len(rivers) >= i + 1:
                    print('\t<river>' + rivers[i].strip() + '</river>', end="\n", file=w)
                else:
                    print('\t<river></river>', end="\n", file=w)

                print('\t</geo>', end="\n", file=w)

        else:

            print('\t<geo>', end="\n", file=w)
            print('\t<geotype>' + row[27].strip() + '</geotype>', end="\n", file=w)
            print('\t<city>' + row[28].strip() + '</city>', end="\n", file=w)
            print('\t<state>' + row[29].strip() + '</state>', end="\n", file=w)
            print('\t<county>' + row[30].strip() + '</county>', end="\n", file=w)
            print('\t<country>' + row[31].strip() + '</country>', end="\n", file=w)
            print('\t<region>' + row[32].strip() + '</region>', end="\n", file=w)
            print('\t<subregion>' + row[33].strip() + '</subregion>', end="\n", file=w)
            print('\t<locale>' + row[34].strip() + '</locale>', end="\n", file=w)
            print('\t<locus>' + row[35].strip() + '</locus>', end="\n", file=w)
            print('\t<excavation>' + row[36].strip() + '</excavation>', end="\n", file=w)
            print('\t<river>' + row[37].strip() + '</river>', end="\n", file=w)
            print('\t</geo>', end="\n", file=w)



        myclassification = row[38].strip()
        if '|' in myclassification:
            myclassifications = myclassification.split('|')
            print('\t<Classification>' + myclassifications[0].strip() + '</Classification>', end="\n", file=w)
            print('\t<Classification>' + myclassifications[1].strip() + '</Classification>', end="\n", file=w)
        else:
            print('\t<Classification>' + row[38].strip() + '</Classification>', end="\n", file=w)



        print('\t<RightsandReproduction>'+row[39].strip()+'</RightsandReproduction>',end="\n",file=w)
        print('\t<LinkResource>'+row[40].strip()+'</LinkResource>',end="\n",file=w)
        print('\t<MetadataDate>'+row[41].strip()+'</MetadataDate>',end="\n",file=w)
        print('\t<Repository>'+row[42].strip()+'</Repository>',end="\n",file=w)
        print('</metobject>',end="\n",file=w)

        #print(row[25].strip())
        #dimension = row[25].strip()

        #m1 = re.search(r'(Diam). *(\d*\/\d*) *(in). *\((\d*.*\d) *(cm)\)', dimension)

        #if m1:
#            print(m1.group(1), m1.group(2), m1.group(3), m1.group(4), m1.group(5))




print('</metmuseum>',end="\n",file=w)


f.close()
w.close()


w = open('newmetsample.xml','r',encoding='utf8')
y = open('metsamplevalidation.xml','w',encoding='utf8')
y.close()
y = open('metsamplevalidation.xml','a',encoding='utf8')




for line in w:
    line.replace('&','&amp;')
    y.write(line)
w.close()
y.close()

