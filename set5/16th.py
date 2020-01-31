import json
import time
import codecs
import requests

def get_data_from_url(url, headers={}):
    r = requests.get(url, headers=headers)
    if not r.ok:
        r.raise_for_status()
    
    return r.text
    #decoded = r.json()
    #return decoded

def get_abstracts_from_pubmed(count, query, nextCursorMark=None):
    url_pattern = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={query}&resulttype=core&format=json&pageSize={count}&cursorMark={nextCursorMark}'

    if nextCursorMark is None:
        nextCursorMark='*'

    url = url_pattern.format(count=count, query=query, nextCursorMark=nextCursorMark)
    
    print ('URL:')
    print (url)
    
    data = get_data_from_url(url)
#    return [{'title': x['title'], 'abstract': x['abstractText']} for x in data['resultList']['result'] 
#            if 'title'in x and 'abstractText'in x]

    return data

def save_abstracts(query, hitcount):

    to_fetch = min(1000, hitcount)
    
    data=get_abstracts_from_pubmed(to_fetch, query)
    
    fetched = to_fetch
    output_filename = 'abstracts.json'
    output_f = codecs.open(output_filename, 'w', 'utf-8')
    while True:
        parsed = json.loads(data)
        nextCursorMark=parsed['nextCursorMark']
        
        output_f.write(data + '\n')
        output_f.flush()
        print ('Fetched:', fetched)
        
        if fetched >= hitcount:
            break
        
        time.sleep(3)
        data = get_abstracts_from_pubmed(1000, query, nextCursorMark)
        fetched += 1000
        
        
        
    output_f.close()
    
save_abstracts('Greece', 10000)

data = []
with open('abstracts.json') as f:
    for l in f:
        temp_data = json.loads(l)
        if not 'resultList' in temp_data:
            continue
            
        if not 'result' in temp_data['resultList']:
            continue
            
        for result in temp_data['resultList']['result']:
            if not 'title' in result:
                continue
                
            title = result['title']
            
            if not 'abstractText' in result:
                continue
                
            abstract = result['abstractText']
            
            data.append(abstract)

abstracts=[i.replace(",", "").replace(".", "").replace('-','').replace('(','').replace(')','').lower() for i in data]
temp=[]
words={}
with open('wordsfreq.txt') as f:
    for line in f:
        for word in line.split():
            temp.append(word.lower())
for i in range(0,len(temp)-1,2):
    words[temp[i]]=int(temp[i+1])
with open('word_cloud.txt','w+') as f:
    for abstract in abstracts:
        for word in abstract.split():
            if word in words.keys() and words[word]<10000:
                f.write(word+' ')            

#################
###In terminal###
#################                
#wordcloud_cli \
#   --text word_cloud.txt \
#   --imagefile wordclound.png \
#   --width 1000 --height 1000 \
#   --mask gr.jpg

