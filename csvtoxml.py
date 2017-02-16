#met museum csv


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

        artistlist1 = {}
        artistlist2 = {}

        myartistrole = row[12].strip()
        myartistassociation = row[13].strip()
        myartistdisplayname = row[14].strip()
        myartistdisplaybio = row[15].strip()
        myartistnationality = row[18].strip()
        myartistbegin = row[19].strip()
        myartistend = row[20].strip()




        if '|' in myartistrole or '|' in myartistassociation or '|' in myartistdisplayname or '|' in myartistdisplaybio or '|' in myartistnationality or '|' in myartistbegin or '|' in myartistend:

            if '|' in myartistrole:
                myartists = myartistrole.split('|')
                artistlist1['role'] = myartists[0]
                artistlist2['role'] = myartists[1]
            else:
                artistlist1['role'] = myartistrole.strip()
                artistlist2['role'] = ''


            if '|' in myartistassociation:
                myartists = myartistassociation.split('|')
                artistlist1['association'] = myartists[0]
                artistlist2['association'] = myartists[1]
            else:
                artistlist1['association'] = myartistassociation.strip()
                artistlist2['association'] = ''

            if '|' in myartistdisplayname:
                myartists = myartistdisplayname.split('|')
                artistlist1['displayname'] = myartists[0]
                artistlist2['displayname'] = myartists[1]
            else:
                artistlist1['displayname'] = myartistdisplayname.strip()
                artistlist2['displayname'] = ''

            if '|' in myartistdisplaybio:
                myartists = myartistdisplaybio.split('|')
                artistlist1['displaybio'] = myartists[0]
                artistlist2['displaybio'] = myartists[1]
            else:
                artistlist1['displaybio'] = myartistdisplaybio.strip()
                artistlist2['displaybio'] = ''

            if '|' in myartistnationality:
                myartists = myartistnationality.split('|')
                artistlist1['nationality'] = myartists[0]
                artistlist2['nationality'] = myartists[1]
            else:
                artistlist1['nationality'] = myartistnationality.strip()
                artistlist2['nationality'] = ''

            if '|' in myartistbegin:
                myartists = myartistbegin.split('|')
                artistlist1['artistbegin'] = myartists[0]
                artistlist2['artistbegin'] = myartists[1]
            else:
                artistlist1['artistbegin'] = myartistbegin.strip()
                artistlist2['artistbegin'] = ''

            if '|' in myartistend:
                myartists = myartistend.split('|')
                artistlist1['artistend'] = myartists[0]
                artistlist2['artistend'] = myartists[1]
            else:
                artistlist1['artistend'] = myartistend.strip()
                artistlist2['artistend'] = ''


            print('\t<artist>', end="\n", file=w)
            print('\t<artistrole>' + artistlist1['role'].strip() + '</artistrole>', end="\n", file=w)
            print('\t<artistassociation>' + artistlist1['association'].strip() + '</artistassociation>', end="\n", file=w)
            print('\t<displayname>' + artistlist1['displayname'].strip() + '</displayname>', end="\n", file=w)
            print('\t<displaybio>' + artistlist1['displaybio'].strip() + '</displaybio>', end="\n", file=w)
            print('\t<nationality>' + artistlist1['nationality'].strip() + '</nationality>', end="\n", file=w)
            print('\t<artistbegin>' + artistlist1['artistbegin'].strip() + '</artistbegin>', end="\n", file=w)
            print('\t<artistend>' + artistlist1['artistend'].strip() + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)

            print('\t<artist>', end="\n", file=w)
            print('\t<artistrole>' + artistlist2['role'].strip() + '</artistrole>', end="\n", file=w)
            print('\t<artistassociation>' + artistlist2['association'].strip() + '</artistassociation>', end="\n",file=w)
            print('\t<displayname>' + artistlist2['displayname'].strip() + '</displayname>', end="\n", file=w)
            print('\t<displaybio>' + artistlist2['displaybio'].strip() + '</displaybio>', end="\n", file=w)
            print('\t<nationality>' + artistlist2['nationality'].strip() + '</nationality>', end="\n", file=w)
            print('\t<artistbegin>' + artistlist2['artistbegin'].strip() + '</artistbegin>', end="\n", file=w)
            print('\t<artistend>' + artistlist2['artistend'].strip() + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)

        else:

            print('\t<artist>', end="\n", file=w)
            print('\t<artistrole>' + row[13].strip() + '</artistrole>', end="\n", file=w)
            print('\t<artistassociation>' + row[13].strip() + '</artistassociation>', end="\n", file=w)
            print('\t<displayname>' + row[14].strip() + '</displayname>', end="\n", file=w)
            print('\t<displaybio>' + row[15].strip() + '</displaybio>', end="\n", file=w)
            print('\t<nationality>' + row[18].strip() + '</nationality>', end="\n", file=w)
            print('\t<artistbegin>' + row[19].strip() + '</artistbegin>', end="\n", file=w)
            print('\t<artistend>' + row[20].strip() + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)

        if len(artistlist1) > 0:
            print('\t<artist>', end="\n", file=w)
            print('\t\t<artistrole>' + artistlist1['role'] + '</artistrole>',end="\n", file=w)
            print('\t\t<artistassociation>' + artistlist1['role'] + '</artistassociation>', end="\n", file=w)
            print('\t\t<displayname>' + artistlist1['role'] + '</displayname>', end="\n", file=w)
            print('\t\t<displaybio>' + artistlist1['role'] + '</displaybio>', end="\n", file=w)
            print('\t\t<nationality>' + artistlist1['role'] + '</nationality>', end="\n", file=w)
            print('\t\t<artistbegin>' + artistlist1['role'] + '</artistbegin>', end="\n", file=w)
            print('\t\t<artistend>' + artistlist1['role'] + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)

        if len(artistlist2) > 0:
            print('\t<artist>', end="\n", file=w)
            print('\t\t<artistrole>' + artistlist2['role'] + '</artistrole>',end="\n", file=w)
            print('\t\t<artistassociation>' + artistlist2['role'] + '</artistassociation>', end="\n", file=w)
            print('\t\t<displayname>' + artistlist2['role'] + '</displayname>', end="\n", file=w)
            print('\t\t<displaybio>' + artistlist2['role'] + '</displaybio>', end="\n", file=w)
            print('\t\t<nationality>' + artistlist2['role'] + '</nationality>', end="\n", file=w)
            print('\t\t<artistbegin>' + artistlist2['role'] + '</artistbegin>', end="\n", file=w)
            print('\t\t<artistend>' + artistlist2['role'] + '</artistend>', end="\n", file=w)
            print('\t</artist>', end="\n", file=w)


        print('\t<ObjectDate>'+row[21].strip()+'</ObjectDate>',end="\n",file=w)
        print('\t<ObjectBeginDate>'+row[22].strip()+'</ObjectBeginDate>',end="\n",file=w)
        print('\t<ObjectEndDate>'+row[23].strip()+'</ObjectEndDate>',end="\n",file=w)

        temp = row[24].replace(' or ', ',')
        temp = temp.replace('and ', ',')

        mymateriallist = temp.split(',')



        for item in mymateriallist:
            print('\t<Medium>'+item.strip()+'</Medium>',end="\n",file=w)






        m1 = re.search(r'(Diam). *(\d*\/\d*) *(in). *\((\d*.*\d) *(cm)\)', row[25].strip())
        m2 = re.search(r'^H\.\s.*?([^in]+)(in).\s\(([^cm]+)(cm)\)', row[25].strip())   #just height' but exclude m2b
        m2a = re.search(r'(H)\.\s([^in]+)(in).\s\(([^cm]+)(cm)\);\s*(Diam).\s*([^in]+)(in).\s*\(([^cm]+)(cm)\)', row[25].strip())   #height and diam
        m2b = re.search(r'(\w*):\s(H).\s([^in]+)(in).\s\(([^cm]+)(cm)\)', row[25].strip()) # label with height
        m3 = re.search(r'(^\d.*) x (\d.*) x (\d.*) (in).*\((\d.*) x (\d.*) x (\d.*)(cm)\)', row[25].strip())   # 3 dimensions with no label
        m4 = re.search(r'(?P<label>\w*):\s(?P<first>.*?)(\sx\s(?P<second>.*?))?(\sx\s(?P<third>.*?))?\s(?P<units>\w*?\.?)\s\((?P<first_metric>\d*\.?\d*)(\sx\s(?P<second_metric>\d*\.?\d*))?(\sx\s(?P<third_metric>\d*\.?\d*))?\s(?P<metric_unit>\w*)\);\s(?P<imp_weight1>\d*(\.?\d*))\s(?P<imp_weight_unit_1>\w*\.?)\s(?P<imp_weight2>\d*(\.?\d*))\s(?P<imp_weight_unit_2>\w*\.?)\s\((?P<metric_weight>\d*\.?\d*)\s(?P<metric_weight_unit>\w*)', row[25].strip())
        m4a = re.search(r'(?P<label>\w*):\s(?P<first>.*?)(\sx\s(?P<second>.*?))?\s(?P<units>\w*?\.?)\s\((?P<first_metric>\d*\.?\d*)(\sx\s(?P<second_metric>\d*\.?\d*))??\s(?P<metric_unit>\w*)\);\s(?P<imp_weight1>\d*(\.?\d*))\s(?P<imp_weight_unit_1>\w*\.?)\s(?P<imp_weight2>\d*(\.?\d*))\s(?P<imp_weight_unit_2>\w*\.?)\s\((?P<metric_weight>\d*\.?\d*)\s(?P<metric_weight_unit>\w*)',row[25].strip())




        if m1:  # just diameter

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

        if m2 and not m2a:

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


        if m2a:
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

        if m2b:
            if len(m2b.groups()) == 6:

                print('\t<DimensionsFeature>', end="\n", file=w)

                if m2b.group(4).find("in") > -1:
                    print('\t<feature>' + m2b.group(1).strip() + '</feature>', end="\n", file=w)
                    print('\t\t<DimensionsSet>', end="\n", file=w)
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m2b.group(3).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                if m2b.group(6).find("in") > -1:
                    print('\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t<dimensionvalue>' + m5.group(5).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t</Dimension>', end="\n", file=w)

                    print('\t\t</DimensionsSet>', end="\n", file=w)

                print('\t</DimensionsFeature>', end="\n", file=w)


        if m3:
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

            if len(m4.groups()) == 21:


                print('\t<DimensionsFeature>', end="\n", file=w)

                if m4.group(7).find("in") > -1:
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
                    print('\t\t\t\t<dimensionvalue>' + m4.group(4).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'inches' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(6).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t</DimensionsSet>', end="\n", file=w)

                if m4.group(13).find("cm") > -1:
                    print('\t\t<DimensionsSet>', end="\n", file=w)
                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Height' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(8).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Width' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(10).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t\t<Dimension>', end="\n", file=w)
                    print('\t\t\t\t<dimensiontype>' + 'Depth' + '</dimensiontype>', end="\n", file=w)
                    print('\t\t\t\t<dimensionunit>' + 'centimeters  ' + '</dimensionunit>', end="\n", file=w)
                    print('\t\t\t\t<dimensionvalue>' + m4.group(12).strip() + '</dimensionvalue>', end="\n", file=w)
                    print('\t\t\t</Dimension>', end="\n", file=w)

                    print('\t\t</DimensionsSet>', end="\n", file=w)

                print('\t</DimensionsFeature>', end="\n", file=w)

        if m4a:  #ovrall example label and 3 dimension

            if len(m4a.groups()) == 17:


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
#\w*:\s[^x]+x\s[^x]+x\s[^in]+\w*

#ddddd