import requests,re,matplotlib
import networkx as nx

def f(x,i):
    url = 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'
    r = requests.get(url)
    obo = r.text
    l=re.findall('id: (.*)\nname: '+x,obo)
    x=l[0]
    l=re.findall('id: (.*)\nname: '+i,obo)
    i=l[0]
    G=nx.Graph()
    G.add_node(x)
    G.add_node(i)
    while True:
        if l[0]=='HP:0000001':
            l=['mitsos']
            break
        else:
            l=re.findall('id: '+x+'.*?is_a: (HP:\d+) !',obo,re.S)
            y=l[0]
            G.add_node(y)
            G.add_edge(x,y)
            x=y
    while True:
        if l[0]=='HP:0000001':
            l=['mitsos']
            break
        else:
            l=re.findall('id: '+i+'.*?is_a: (HP:\d+) !',obo,re.S)
            y=l[0]
            G.add_node(y)
            G.add_edge(i,y)
            i=y
    return nx.draw(G,with_labels=True)

#f('Oligoclonal elevation of circulating IgG', 'Renotubular dysgenesis')
f('Enlarged epiphyses of the 4th toe', 'Long hallux')
#f('Abnormality of the pharynx', 'Abnormal Sharpey fiber morphology')
#f('Visual gaze preference', 'Medium chain dicarboxylic aciduria')