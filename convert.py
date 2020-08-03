import os
import json

import xml.etree.ElementTree as ElemTree

if __name__ == "__main__":
	rootDir = os.getcwd()
	annotationDir = os.path.join(rootDir, "annoteringsdownloads")
	filePath = os.path.join(annotationDir, "via_export_json.json")
	outPath = os.path.join(rootDir, "Annotations")	

	#
	#
	#

	jsonFile = open(filePath)
	jsonString = jsonFile.read()
	jsonObj = json.loads(jsonString)

	#
	#
	#

	for imageObj in jsonObj.values():
		xmlRootElement = ElemTree.Element('annotation')
		xmlFolderElement = ElemTree.SubElement(xmlRootElement, 'folder')
		xmlNameElement = ElemTree.SubElement(xmlRootElement, 'name')
		xmlRegionsElement = ElemTree.SubElement(xmlRootElement, 'regions')

		#
		#
		#

		xmlFolderElement.text = "Folder"
		xmlNameElement.text = imageObj['filename']

		#
		#
		#

		if len(imageObj['regions']) >= 1:
			for imageRegion in imageObj['regions']:
				xmlShapeRootElement = ElemTree.SubElement(xmlRegionsElement, 'shape')
				#xmlShapeXElement = ElemTree.SubElement(xmlShapeRootElement, 'x')
				#xmlShapeYElement = ElemTree.SubElement(xmlShapeRootElement, 'y')
				#xmlShapeWidthElement = ElemTree.SubElement(xmlShapeRootElement, 'width')	
				#xmlShapeHeightElement = ElemTree.SubElement(xmlShapeRootElement, 'height')

				xmlShapePositionElement = ElemTree.SubElement(xmlShapeRootElement, 'position', x=str(imageRegion['shape_attributes']['x']), y=str(imageRegion['shape_attributes']['y']))
				xmlShapeDimensionElement = ElemTree.SubElement(xmlShapeRootElement, 'dimension', width=str(imageRegion['shape_attributes']['width']), height=str(imageRegion['shape_attributes']['height']))

				#
				#
				#

				#xmlShapeXElement.text = '1'
				#xmlShapeYElement.text = '2'
				#xmlShapeWidthElement.text = '23'
				#xmlShapeHeightElement.text = '42' 


		name,extension = os.path.splitext(imageObj['filename'])
		xmlTree = ElemTree.ElementTree(xmlRootElement)
		xmlTree.write(os.path.join(outPath, name + '.xml'))
