sizes = {
                'chr1':    249250621,
                'chr2':    243199373,
                'chr3':    198022430,
                'chr4':    191154276,
                'chr5':    180915260,
                'chr6':    171115067,
                'chr7':    159138663,
                'chrX':    155270560,
                'chr8':    146364022,
                'chr9':    141213431,
                'chr10':   135534747,
                'chr11':   135006516,
                'chr12':   133851895,
                'chr13':   115169878,
                'chr14':   107349540,
                'chr15':   102531392,
                'chr16':   90354753,
                'chr17':   81195210,
                'chr18':   78077248,
                'chr20':   63025520,
                'chrY' :   59373566,
                'chr19':   59128983,
                'chr22':   51304566,
                'chr21':   48129895,
                'chrMT' :   16571,
                }
class Position():
    def __init__(self,chromosome,start,end):
        self.chromosome=chromosome
        self.start=start
        self.end=end
        if start not in range(sizes[chromosome]) or end not in range(sizes[chromosome]) or start>end:
            raise Exception('Invalid input')
    def check_position(chromosome,start):
        return chromosome in sizes.keys() and start in range(sizes[chromosome])
    def __str__(self):
        return '`{}, {}-{}`'.format(self.chromosome,self.start,self.end)
    def __len__(self,):
        return abs(self.end - self.start)
class Mutation(Position):
    def __init__(self,chromosome,start,end,reference,alternative):
        self.chromosome=chromosome
        self.start=start
        self.end=end
        self.reference=reference
        self.alternative=alternative
        bases='ACGT'
        for rbase in reference:
            for abase in alternative:
                if rbase not in bases or abase not in bases:
                    raise Exception('Reference/alternative can only be DNA bases')
        if reference==alternative:
            raise Exception('Alternative and reference cannot be the same')
        if len(reference)!=(len(self)):            
            raise Exception('length of reference not equal to length of position')
    def type(self,):
        if len(self.reference)==1 and len(self.alternative)==1:
            return 'SNP'
        if len(self.reference)!=1 and len(self.alternative)!=1 and len(self.reference)==len(self.alternative):
            return "substitution"
        if len(self.reference)==0 and len(self.alternative)>0:
            return "insertion"
        if len(self.reference)>0 and len(self.alternative)==0:
            return "deletion"
        else:
            return 'complex situation'
    def __str__(self):
        return '{}, {}-{} {}>{}'.format(self.chromosome,self.start,self.end,self.reference,self.alternative)
m = Mutation('chr5', start=10000, end=10000, reference='', alternative='AT')
print(str(m))
m.type()
