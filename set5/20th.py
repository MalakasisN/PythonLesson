import matplotlib.pyplot as plt
from Bio import Entrez,SeqIO

def get_chunks(dna, window_size=500, stride=30):
    for i in range(0, len(dna) - window_size + 1, stride):
        chunk = dna[i:i + window_size]
        assert len(chunk) == window_size
        yield chunk

def window_gc_content(seq):
    windowgc=[]
    for chunk in get_chunks(seq):
        gc=(chunk.count('G')+chunk.count('C'))/len(chunk)
        windowgc.append(gc)
    return windowgc


search_term = 'MN908947.3 OR NC_004718.3'
handle = Entrez.esearch(db='nucleotide', term=search_term)
genome_ids = Entrez.read(handle)['IdList']
genomes=[]
for genome_id in genome_ids:
    record = Entrez.efetch(db="nucleotide", id=genome_id, rettype="gb", retmode="text")

    filename = 'genBankRecord_{}.gb'.format(genome_id)
    with open(filename,'w+') as f:
        f.write(record.read())
    SeqIO.convert(filename, "genbank", filename+".fasta", "fasta")
    with open(filename+".fasta") as f:
        x=''
        for i in f.readlines()[1:]:
            x+=i.replace('\n','')
        genomes.append(x)
Wuhan=genomes[0]
Sars=genomes[1]
Wuhany=window_gc_content(Wuhan)
Sarsy=window_gc_content(Sars)
Wuhanx=[]
Sarsx=[]
for i in range(len(Wuhany)):
    Wuhanx.append(i*30)
for i in range(len(Sarsy)):
    Sarsx.append(i*30)
fig, (ax1,ax2) = plt.subplots(nrows=2)
ax1.plot(Wuhanx,Wuhany)
ax1.legend('Wuhan')
ax2.plot(Sarsx,Sarsy,c='red')
ax2.legend('SARS')
plt.show()