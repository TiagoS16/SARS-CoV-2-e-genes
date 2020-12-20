from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read(open('FGG.gb'), format='gb' )

result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)

with open("FBB_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()


