string="bquick-{fox}"
import re
pattern=r"brown-{fox}"
match=re.search(pattern,string)
if match:
    print("found")
else:
    print("not found")