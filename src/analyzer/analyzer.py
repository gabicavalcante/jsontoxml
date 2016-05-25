from xml.dom import minidom


from src.analyzer import costs, actions
from src.analyzer.resources import analyzer_resource

xml_path = 'xml/xml-output.xml'


def run():
    f = open("analyzer.log", 'a+')
    f.write("############# ANALYZER #############\n\n")
    f.close()

    doc = minidom.parse(xml_path)
    actions.run(doc.getElementsByTagName("data"))
    costs.run(doc.getElementsByTagName("data"))
    analyzer_resource(xml_path)
