import xml.etree.ElementTree as ET


def process_ul(ul_element):
    output = {}
    for element in ul_element.iter('li'):
        key = element[0].text
        text = [child.tail.strip() for child in element]
        output[key] = text[0]

    return output


def main():
    magic = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" [
            <!ENTITY nbsp ' '>
            ]>'''
    f = open('testsample.html')
    contents = f.read()

    root = ET.XML(magic + contents)
    print(process_ul(root))

if __name__ == '__main__':
    main()
