from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import re
def convert_sequence_to_fast(sequence, fasta_filename, id, description):
    sequence = Seq(sequence)
    # http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
    sequence_record = SeqRecord(sequence, id=id, description=description)

    with open(fasta_filename, "w") as output_handle:
        SeqIO.write(sequence_record, output_handle, "fasta")

def blat_fasta(fasta_filename, output_filename):
    fasta_string = open(fasta_filename).read()
    result_handle = NCBIWWW.qblast(
        "blastn",
        "GPIPE/9606/105/ref_top_level", 
        fasta_string, 
        short_query=True,
        expect=1000,
        nucl_reward=1,
        nucl_penalty=-3,
        filter='F',
    )
    
    with open(output_filename, "w") as out_handle:
        out_handle.write(result_handle.read())

def parse_BLAT_output(blat_filename):
    result_handle = open(blat_filename)
    blast_records = NCBIXML.parse(result_handle)
    E_VALUE_THRESH = 0.04
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    for i in hsp.match:
                        if i!='|':
                            alt=hsp.query[hsp.match.index(i)]
                            ref=hsp.sbjct[hsp.match.index(i)]
                            chrom=re.compile('chromosome (\d+)')
                            chromatch=chrom.findall(alignment.title)
                            chrnum=list(chromatch)[0]
                            asem=re.compile('(GRCh\d+)')
                            asematch=asem.findall(alignment.title)
                            asenum=list(asematch)[0]
                            position = hsp.sbjct_start+hsp.match.index(i)
                            break
                    return chrnum,position,ref,alt,asenum
def f(myseq):
    convert_sequence_to_fast(myseq, 'example.fasta', 'mitsos', 'my precious sequence')
    blat_fasta('example.fasta', 'example_blat_results.xml')
    output=parse_BLAT_output('example_blat_results.xml')
    try:
        result={'chromosome':output[0],'position':output[1],'reference':output[2],'alternative':output[3],'assembly':output[4]}
        return result
    except:
        return None
    
    
print(f('GAAGACGATGCTGTAGATGAAGAGCCCCA'))