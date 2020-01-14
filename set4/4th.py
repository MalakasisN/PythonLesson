import re
txt='''
HPK12347
'''
pattern=re.compile(r'[A|B|E|Z|H|I|K|M|N|O|P|T|Y|X]{2,3}[^0\D]\d{3}$')
matches=pattern.findall(txt)
if matches==[]:
    print('NOT OK')
else:
    print('OK')