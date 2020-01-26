import requests, sys

def f(rsid):
    server = "http://myvariant.info/v1/query?"
    ext = "q="
    Diseases=[]
    r = requests.get(server+ext+rsid, headers={ "Content-Type" : "text/plain"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    rj=r.json()
    try:
        clinvar=rj['hits'][0]['clinvar']
        if type(clinvar['rcv']) is list:
            for i in clinvar['rcv']:
                Diseases.append(i['conditions']['name'])
        elif type(clinvar['rcv']) is dict:
            Diseases.append(clinvar['rcv']['conditions']['name'])
    except:
        pass
    return Diseases
print(f('rs80359876')) #Multiple diseases
print(f('rs374032054')) #Single disease
print(f('rs766444643')) #No disease