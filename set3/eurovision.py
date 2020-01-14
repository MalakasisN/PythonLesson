import pandas as pd

df = pd.read_excel('ESC-2016-grand_final-full_results.xls') # Αγνοήστε τα warnings..

data = []

for k,v in df.to_dict('index').items():
    if k==0:
        continue
    
    d = {
        'from_country': v['Eurovision Song Contest 2016 Grand Final'],
        'to_country': v['Unnamed: 1'],
        'jury_points': 0 if v['Unnamed: 9']=='\n' else int(v['Unnamed: 9']),
        'televote_points': 0 if v['Unnamed: 10']=='\n' else int(v['Unnamed: 10']),
    }
    
    data.append(d)