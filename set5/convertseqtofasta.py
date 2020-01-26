from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def convert_sequence_to_fast(sequence, fasta_filename, id, description):
    sequence = Seq(sequence)
    # http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc16
    sequence_record = SeqRecord(sequence, id=id, description=description)

    with open(fasta_filename, "w") as output_handle:
        SeqIO.write(sequence_record, output_handle, "fasta")

convert_sequence_to_fast('AGAAGACGATGCTGTAGATGAAGAGCCCCA', 'example.fasta', 'mitsos', 'my precious sequence')