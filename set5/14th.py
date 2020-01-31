import requests,re,matplotlib
import networkx as nx

def f(x,i):
    a=x
    b=i
    url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
    r = requests.get(url)
    obo = r.text
    l=['mitsos']
    G=nx.Graph()
    G.add_node(x)
    G.add_node(i)
    while True:
        if l[0]=='HP:0000001':
            l=['mitsos']
            break
        else:
            l=re.findall('name: '+x+'.*?is_a: (HP:\d+) !',obo,re.S)
            y='id: '+l[0]
            ll=re.findall(y+'\nname: (.*)',obo)
            y=ll[0]
            G.add_node(y)
            G.add_edge(x,y)
            x=y
    while True:
        if l[0]=='HP:0000001':
            l=['mitsos']
            break
        else:
            l=re.findall('name: '+i+'.*?is_a: (HP:\d+) !',obo,re.S)
            y='id: '+l[0]
            ll=re.findall(y+'\nname: (.*)',obo)
            y=ll[0]
            G.add_node(y)
            G.add_edge(i,y)
            i=y

    return len(nx.shortest_path(G, source=a, target=b))

print(f('Oligoclonal elevation of circulating IgG', 'Renotubular dysgenesis'))             