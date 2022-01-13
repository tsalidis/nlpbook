
import re

m = re.compile("γλωσσολογία", flags=(re.IGNORECASE | re.UNICODE) )

r = m.findall("Υπολογιστική Γλωσσολογία!")

print(r)
if r:
  print("Success")
else:
  print("Fail")