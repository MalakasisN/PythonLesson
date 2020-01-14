import re
txt='''
abcd123defg456kkk777
'''
pattern=re.compile(r'\d([^\d]+)\d')
matches=pattern.findall(txt)
print(matches)
