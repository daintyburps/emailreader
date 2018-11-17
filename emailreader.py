import xml.etree.ElementTree as ET

f = open('testsample.html')

contents = f.read()

tree = ET.fromstring(contents)
print(len(tree))
for child in tree:
	print(child)
	print(child.text)
	for c in child:
		print(c.text)

# print(tree.)
# print(root)
# print(parsed_html)
