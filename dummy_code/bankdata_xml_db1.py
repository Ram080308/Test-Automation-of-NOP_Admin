
import xml.etree.ElementTree as ET

tree = ET.parse("BankData.xml")
root = tree.getroot()
l = len(root)
print(l)

for items in root.iter():
    if items.tag == "note":
        amount = items.text
        print(amount)
