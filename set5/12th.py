import requests,random
import networkx as nx
import matplotlib.pyplot as plt

def links(page):
    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": page,
        "prop": "links",
        'pllimit':100,
    }

    URL = "https://en.wikipedia.org/w/api.php"
    S = requests.Session()
    R = S.get(url=URL, params=PARAMS)
    
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    ret = []
    for k, v in PAGES.items():
        for l in v.get("links", []):
            to_append = l["title"]
            
            if 'Category' in to_append:
                continue
                
            if 'Wikipedia' in to_append:
                continue
            
            if 'Digital object identifier' in to_append:
                continue
                
            if 'International Standard Book Number' in to_append:
                continue
                
            if 'Template' in to_append:
                continue
                
            ret.append(to_append)
    
    return ret

    

G=nx.Graph()
x='bioinformatics'
k=100
for i in range(k):    
    G.add_node(x)
    l=links(x)
    ll=random.choices(l,k=5)
    for j in ll:
        G.add_node(j)
        G.add_edge(x,j)
    y=random.choice(ll)
    temp=links(y)
    if temp==[]:
        print(y)
        k+=1
        pass
    else:
        x=y
        
    


pos=nx.spring_layout(G)

nx.draw(G, pos=pos, with_labels=False, node_size= 10, node_color='green')
nx.draw_networkx_labels(G, pos=pos, labels={'bioinformatics': 'bioinformatics'}, font_size=10, font_color='red')