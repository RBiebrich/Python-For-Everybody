from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

print ('\n\n')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print ('Retrieving', address)
xml = urlopen(address, context=ctx).read()

print('Retrieved', len(xml), 'characters')
data = xml.decode()
tree = ET.fromstring(data)
#print (data)
counts = tree.findall('.//comment')
tot = 0
for tag in counts:
    num = int(tag.find('count').text)
    tot = tot + num

print('Sum:', tot)

print ('\n\n')