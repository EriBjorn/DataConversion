import pandas as pd
import xml.etree.cElementTree as ET

dataForAlleBildene = pd.read_csv("via_export_csv.csv") # henter inn all data fra csvfil


dataForAlleBildene.head(7) # displays the 5 first elements of the csv file
dataForAlleBildene.iloc[1] # collects all the data from the object with index 1, ps index starts on 0.
dataForAlleBildene.iloc[1].region_shape_attributes.split(',') # readys the data to generate XML file
xText = dataForAlleBildene.iloc[1].region_shape_attributes.split(',')[1].split(':')[1]
yText = dataForAlleBildene.iloc[1].region_shape_attributes.split(',')[2].split(':')[1]
widthTEXT = dataForAlleBildene.iloc[1].region_shape_attributes.split(',')[3].split(':')[1]
heightTEXT = dataForAlleBildene.iloc[1].region_shape_attributes.split(',')[4].split(':')[1]


xText
yText
widthTEXT
heightTEXT[:-1] # obs :-1 or else the last curly bracket in "height:187" get's included




root = ET.Element("annotaion")
folder = ET.SubElement(root, "Folder")



filename = ET.SubElement(root, "new_annotations")
size = ET.SubElement(root, "size")
width = ET.SubElement(size, "width")
height = ET.SubElement(size, "height")
depth = ET.SubElement(size, "depth")

filename.text = dataForAlleBildene.iloc[1].filename
folder.text = "VOC2007"  # CONSTANT
width.text = widthTEXT
height.text = heightTEXT[:-1]
depth.text = "3"     # CONSTANT

tree = ET.ElementTree(root)
tree.write("new_annotations.xml")

