
import re

m = re.compile("(\\w+)(\\s+)(\\w+)", flags=(re.IGNORECASE | re.UNICODE) ) 

TEXT_1   = "one      example";
TEXT_2   = "ενα      παραδειγμα";

group_1 = re.findall(m, TEXT_1)[0]
group_2 = re.findall(m, TEXT_2)[0]

trimmed_1 = str(group_1[0]) + ' ' + str(group_1[2])
trimmed_2 = str(group_2[0]) + ' ' + str(group_2[2])

print(trimmed_1)
print(trimmed_2)
