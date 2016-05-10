from lxml import etree

countries = ('fr', 'be', 'it', 'mc', 'es', 'ch', 'gb', 'us')

to_remove = []

with open('country.xml', 'r') as f:
    tree = etree.parse(f)

for element in tree.xpath("//record[@model='country.country']"):
    if element.attrib['id'] not in countries:
        to_remove.append(element)

for element in tree.xpath("//record[@model='country.subdivision']"):
    if element.attrib['id'][0:2] not in countries:
        to_remove.append(element)

for element in to_remove:
    element.getparent().remove(element)

with open('country.xml', 'w') as f:
    f.write('<?xml version="1.0"?>\n')
    tree.write(f, pretty_print=True, encoding='utf-8')
