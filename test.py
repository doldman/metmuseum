import normalise
import lxml
import nltk



normalise.ConvertAttributestoTags()





# from lxml import etree as ET
#
# root = ET.Element('root')
#
# normalise.ProcessTitleStrings(root,'title','衣食住|Attire','|')
#
# print(ET.tostring(root,pretty_print=True,method='xml',encoding='unicode'))





    # dimensions = normalise.DimensionNormalise(root,'dimensions',"Image: 44 5/16 × 9 3/16 in. (112.5 × 23.4 cm)")
# print('one dimension ***********************************************************************')
# print(ET.tostring(dimensions,pretty_print=True,method='xml',encoding='unicode'))
# print('one dimension ***********************************************************************\n\n')
#
#
# print('two dimension ***********************************************************************')
# dimensions = normalise.DimensionNormalise(root,'dimensions',"Image: 44 5/16 × 9 3/16 in. (112.5 × 23.4 cm)\
# Overall with mounting: 80 9/16 × 10 11/16 in. (204.7 × 27.2 cm)")
# print(ET.tostring(dimensions,pretty_print=True,method='xml',encoding='unicode'))
# print('two dimension ***********************************************************************\n\n')
#
# print('three dimension ***********************************************************************')
# dimensions = normalise.DimensionNormalise(root,'dimensions',"Image: 44 5/16 × 9 3/16 in. (112.5 × 23.4 cm)\
# Overall with mounting: 80 9/16 × 10 11/16 in. (204.7 × 27.2 cm)\
# Overall with knobs: 80 9/16 × 12 1/2 in. (204.7 × 31.8 cm)")
# print(ET.tostring(dimensions,pretty_print=True,method='xml',encoding='unicode'))
# print('three dimension ***********************************************************************\n\n')

#These dimensions are then wrapped in parent element - dimensions

# <dimensions>
#     <dimension><value>44 5/16</value><type>Image height</type><unit>inches</unit></dimension>'
#     <dimension><value>112.5</value><type>Image height</type><unit>centimeters</unit></dimension>'
#     <dimension><value>9 3/16</value><type>Image width</type><unit>inches</unit></dimension>'
#     <dimension><value>23.4</value><type>Image width</type><unit>centimeters</unit></dimension>'
#     <dimension><value>80 9/16</value><type>Overall with mounting height</type><unit>inches</unit></dimension>'
#     <dimension><value>204.7</value><type>Overall with mounting height</type><unit>centimeters</unit></dimension>'
#     <dimension><value>10 11/16</value><type>Overall with mounting width</type><unit>inches</unit></dimension>'
#     <dimension><value>27.2</value><type>Overall with mounting width</type><unit>centimeters</unit></dimension>'
#     <dimension><value>80 9/16</value><type>Overall with knobs height</type><unit>inches</unit></dimension>'
#     <dimension><value>204.7</value><type>Overall with knobs height</type><unit>centimeters</unit></dimension>'
#     <dimension><value>12 1/2</value><type>Overall with knobs width</type><unit>inches</unit></dimension>'
#     <dimension><value>31.8</value><type>Overall with knobs width</type><unit>centimeters</unit></dimension>'
# </dimensions>