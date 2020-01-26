import requests, sys

def f(chrom,start,end):
    server = "https://rest.ensembl.org"
    ext = "/sequence/region/human/"
    r = requests.get(server+ext+chrom+':'+str(start)+'..'+str(end)+':1?', headers={ "Content-Type" : "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    return r.text

print(f('3',1000000,1000200)) #inputexample