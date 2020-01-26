import requests, sys
def f(chrom,start,end):
    server = "http://myvariant.info/v1/query?"
    ext = "&fetch_all=TRUE"
    totalmuts=[]
    mutswithrsid=[]
    r = requests.get(server+'q='+chrom+':'+str(start)+'-'+str(end)+ext, headers={ "Content-Type" : "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    rj=r.json()
    totalmuts+=rj['hits']
    while True:
        try:
            r=requests.get(server+'scroll_id='+rj['_scroll_id'], headers={ "Content-Type" : "text/plain"})
            if not r.ok:
                r.raise_for_status()
                sys.exit()
            rj=r.json()
            totalmuts+=rj['hits']
        except:
            break
    for i in totalmuts:
        try:
            mutswithrsid.append((i['_id'],i['gnomad_genome']['rsid']))
        except:
            pass
    return mutswithrsid
print(f('chr1',69000,70000)) #inputexample