# 7.3  Parsing BLAST output
from Bio.Blast import NCBIXML

def parse_BLAT_output(blat_filename):
    result_handle = open(blat_filename)
    blast_records = NCBIXML.parse(result_handle)
    
    E_VALUE_THRESH = 0.04
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print("****Alignment****")
                    print ('Query start:', hsp.query_start)
                    print ('Query end:', hsp.query_end)
                    print ('Subject start:', hsp.sbjct_start)
                    print ('Subject end:', hsp.sbjct_end)
                    print("sequence:", alignment.title)
                    print("length:", alignment.length)
                    print("e value:", hsp.expect)
                    print(hsp.query)
                    print(hsp.match)
                    print(hsp.sbjct)
                    #print (dir(hsp))
                    return alignment, hsp


parse_BLAT_output('example_blat_results.xml')