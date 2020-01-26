#Running BLAST over the Internet
from Bio.Blast import NCBIWWW

def blat_fasta(fasta_filename, output_filename):
    fasta_string = open(fasta_filename).read()
    #result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
    #result_handle = NCBIWWW.qblast("blastn", "Human G+T", fasta_string)
    print ('fasta string:')
    print (fasta_string)
    result_handle = NCBIWWW.qblast(
        "blastn", 
        #"Human G+T",
        #"GPIPE/9606/current/ref_top_level", # GRCH38
        "GPIPE/9606/105/ref_top_level", #GRCH37
        fasta_string, 
        short_query=True,
        expect=1000,
        nucl_reward=1,
        nucl_penalty=-3,
        filter='F',
    )
    
    # Gia th diafora meta3u 'nt' kai 'Human G+T' deite edw:
    # https://ftp.ncbi.nlm.nih.gov/pub/factsheets/HowTo_BLASTGuide.pdf 
    # Source code of qblast: https://biopython.org/DIST/docs/api/Bio.Blast.Applications-pysrc.html
    with open(output_filename, "w") as out_handle:
        out_handle.write(result_handle.read())

blat_fasta('example.fasta', 'example_blat_results.xml')