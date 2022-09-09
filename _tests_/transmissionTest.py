import pycurl
from urllib.parse import urlencode

c = pycurl.Curl()

c.setopt(c.URL, 'https://gw.flespi.io:21213')

post_data = {"ident":"988", "timestamp":1234567890, "position.latitude":59, "position.longitude":48, "position.speed":60, "position.direction":75, "fuel.level":87}
postfields = urlencode(post_data)
c.setopt(c.POSTFIELDS, postfields)
c.perform()
c.close()