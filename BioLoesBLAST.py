from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def BLASTn(arg):
    result_handle = NCBIWWW.qblast('blastn', 'nt', '{}'.format(arg))
    blast_records = NCBIXML.read(result_handle)
    for alignment in blast_records.alignments:
        for hsp in alignment.hsps:
            print('*** Alignment ***')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + "...")
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')

