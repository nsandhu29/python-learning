import sys
import urllib.request
import pdb; pdb.set_trace() # launch debugger
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbuscmd.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, \
                                                                                                                 stopid))

data = u.read()
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.txt)
# print('Command options', sys.argv)
#
# raise SystemExit(0)
