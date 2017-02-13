import csv
import re



f = open('metsample.csv','r',encoding='utf8')
w = open('newmetsample.xml','w',encoding='utf8')
w.close()
w = open('newmetsample.xml','a',encoding='utf8')



w.write

myreader = csv.reader(f,delimiter=',')
print(r'<?xml version="1.0" encoding="UTF-8"?>')
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
        print('\t<Title>'+row[6].strip()+'</Title>',end="\n",file=w)
        print('\t<Culture>'+row[7].strip()+'</Culture>',end="\n",file=w)
        print('\t<Period>'+row[8].strip()+'</Period>',end="\n",file=w)
        print('\t<Dynasty>'+row[9].strip()+'</Dynasty>',end="\n",file=w)
        print('\t<Reign>'+row[10].strip()+'</Reign>',end="\n",file=w)
        print('\t<Portfolio>'+row[11].strip()+'</Portfolio>',end="\n",file=w)

        artistrole1 = []
        artistrole2 = []
        artistprefix1 = []
        artistprefix2 = []
        artistdisplayname1 = []
        artistdisplayname2 = []
        artistbio1 = []
        artistbio2 = []
        artistnationality1 = []
        artistnationality2 = []
        artiststartdate1 = []
        artiststartdate2 = []
        artistenddate1 = []
        artistenddate2 = []


        # myartistrole = row[12].strip()
        # if '|' in myartistrole:
        #
        #     myartists = myartistrole.split('|')
        #     artistrole1.add(myartists[0])
        #     artistrole2.add(myartists[1])
        #
        # myartistprefix = row[13].strip()
        # if '|' in myartistprefix:
        #     myartists = myartistprefix.split('|')
        #     artistprefix1.add(myartists[0])
        #     artistprefix2.add(myartists[1])
        #
        # myartistdisplayname = row[14].strip()
        # if '|' in myartistdisplayname:
        #     myartists = myartistdisplayname.split('|')
        #     artistdisplayname1.add(myartists[0])
        #     artistdisplayname2.add(myartists[1])
        #
        # myartistbio = row[15].strip()
        # if '|' in myartistbio:
        #     myartists = myartistbio.split('|')
        #     artistbio1.add(myartists[0])
        #     artistbio2.add(myartists[1])
        #
        # myartistnationality = row[16].strip()
        # if '|' in myartistnationality:
        #     myartists = myartistnationality.split('|')
        #     artistnationality1.add(myartists[0])
        #     artistnationality2.add(myartists[1])
        #
        # myartiststartdate = row[17].strip()
        # if '|' in myartiststartdate:
        #     myartists = myartiststartdate.split('|')
        #     artiststartdate1.add(myartists[0])
        #     artiststartdate2.add(myartists[1])
        #
        # myartistenddate = row[18].strip()
        # if '|' in myartiststartdate:
        #     myartists = myartiststartdate.split('|')
        #     artistenddate1.add(myartists[0])
        #     artistenddate2.add(myartists[1])


        print('\t<ArtistRole>'+row[12].strip()+'</ArtistRole>',end="\n",file=w)
        print('\t<ArtistPrefix>'+row[13].strip()+'</ArtistPrefix>',end="\n",file=w)
        print('\t<ArtistDisplayName>'+row[14].strip()+'</ArtistDisplayName>',end="\n",file=w)
        print('\t<ArtistDisplayBio>'+row[15].strip()+'</ArtistDisplayBio>',end="\n",file=w)
        print('\t<ArtistSuffix>'+row[16].strip()+'</ArtistSuffix>',end="\n",file=w)
        print('\t<ArtistAlphaSort>'+row[17].strip()+'</ArtistAlphaSort>',end="\n",file=w)
        print('\t<ArtistNationality>'+row[18].strip()+'</ArtistNationality>',end="\n",file=w)
        print('\t<ArtistBeginDate>'+row[19].strip()+'</ArtistBeginDate>',end="\n",file=w)
        print('\t<ArtistEndDate>'+row[20].strip()+'</ArtistEndDate>',end="\n",file=w)
        print('\t<ObjectDate>'+row[21].strip()+'</ObjectDate>',end="\n",file=w)
        print('\t<ObjectBeginDate>'+row[22].strip()+'</ObjectBeginDate>',end="\n",file=w)
        print('\t<ObjectEndDate>'+row[23].strip()+'</ObjectEndDate>',end="\n",file=w)

        temp = row[24].replace(' or ', ',')
        temp = temp.replace('and ', ',')
        #temp = temp.replace()
        mymateriallist = temp.split(',')



        for item in mymateriallist:
            print('\t<Medium>'+item.strip()+'</Medium>',end="\n",file=w)






        m1 = re.search(r'(Diam). *(\d*\/\d*) *(in). *\((\d*.*\d) *(cm)\)', row[25].strip())
        m2 = re.search(r'(^H\.).*(\d.*) *(in). *\((\d*.*\d) *(cm)\)', row[25].strip())
        m3 = re.search(r'(^\d.*) x (\d.*) x (\d.*) (in).*\((\d.*) x (\d.*) x (\d.*)(cm)\)', row[25].strip())
        m4 = re.search(r'(?P<label>\w*):\s(?P<first>.*?)\sx\s(?P<second>.*?)?\sx\s(?P<third>.*?)?\s(?P<units>\w*?\.?)\s\((?P<first_metric>\d*\.?\d*)\sx\s(?P<second_metric>\d*\.?\d*)?\sx\s(?P<third_metric>\d*\.?\d*)?\s(?P<metric_unit>\w*)\);\s(?P<imp_weight1>\d*\.?\d*)\s(?P<imp_weight_unit_1>\w*\.?)\s(?P<imp_weight2>\d*\.?\d*)\s(?P<imp_weight_unit_2>\w*\.?)\s\((?P<metric_weight>\d*)\s(?P<metric_weight_unit>\w*)', row[25].strip())
        m5 = re.search(r'([a-zA-z]*):.*(H).*(\d.*) *(in). *\((\d*.*\d) *(cm)\)', row[25].strip())
        m6 = re.search(r'([a-zA-z]*):(.*)x(.*)x(.*)(in).*\((.*)x(.*)x(.*)(cm)\).* (\d.*) (oz)\. (\d*).*(dwt).*\((\d.*)(g)\)', row[25].strip())


        if m1:

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

        if m2:

            print('\t<DimensionSet>', end="\n", file=w)
            if m2.group(5).find("cm") > -1:
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m2.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)

            if m2.group(3).find("in") > -1:
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m2.group(2).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)
            print('\t</DimensionSet>', end="\n", file=w)

        if m5:

            print('\t<DimensionsFeature>', end="\n", file=w)

            if m5.group(6).find("cm") > -1:
                print('\t<feature>' + m5.group(1).strip() + '</feature>', end="\n", file=w)
                print('\t\t<DimensionsSet>', end="\n", file=w)
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m5.group(5).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)

            if m5.group(4).find("in") > -1:
                print('\t\t<Dimension>', end="\n", file=w)
                print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                print('\t\t\t<dimensionvalue>' + m5.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                print('\t\t</Dimension>', end="\n", file=w)

                print('\t\t</DimensionsSet>', end="\n", file=w)

            print('\t</DimensionsFeature>', end="\n", file=w)

        if m3:

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




        if m4:

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


        print('\t<CreditLine>'+row[26].strip()+'</CreditLine>',end="\n",file=w)
        print('\t<GeographyType>'+row[27].strip()+'</GeographyType>',end="\n",file=w)
        print('\t<City>'+row[28].strip()+'</City>',end="\n",file=w)
        print('\t<State>'+row[29].strip()+'</State>',end="\n",file=w)
        print('\t<County>'+row[30].strip()+'</County>',end="\n",file=w)
        print('\t<Country>'+row[31].strip()+'</Country>',end="\n",file=w)
        print('\t<Region>'+row[32].strip()+'</Region>',end="\n",file=w)
        print('\t<Subregion>'+row[33].strip()+'</Subregion>',end="\n",file=w)
        print('\t<Locale>'+row[34].strip()+'</Locale>',end="\n",file=w)
        print('\t<Locus>'+row[35].strip()+'</Locus>',end="\n",file=w)
        print('\t<Excavation>'+row[36].strip()+'</Excavation>',end="\n",file=w)
        print('\t<River>'+row[37].strip()+'</River>',end="\n",file=w)
        print('\t<Classification>'+row[38].strip()+'</Classification>',end="\n",file=w)
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


        print(row[25].strip())

print('</metmuseum>',end="\n",file=w)

f.close()
w.close()



#(.*)(?<=\:)\s([^x]+)x\s([^x]+)x\s(\d[^in]+)(in)([^\(]+).?(\d[^x]+)x\s([^x]+)x\s(\d[^ cm]+) (cm)\);\s\d[^oz]+
\w*:\s[^x]+x\s[^x]+x\s[^in]+\w*