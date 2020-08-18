from itertools import groupby
s = "aabbbccaa"
"".join([key+str(list(value)) for key,value in groupby(s)])      # a2b3c2a2
import re
re.findall(r"\d","a2b3c2a2")   # [2,3,2,2]
