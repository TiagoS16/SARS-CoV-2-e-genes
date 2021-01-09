from Bio import AlignIO
align = AlignIO.read("entrez_prot.aln", "clustal")
print(align)
print("Number of rows: %i" % len(align))

for record in align:
    print("%s - %s" % (record.seq, record.id))

# how often letters in the alignment are substituted for each other
substitutions = align.substitutions
print(substitutions)

#Histogram of homologous sequence lenghts
from Bio import SeqIO
sizes = [len(rec) for rec in SeqIO.parse("SeqsHomologas_FGG_DNA_blast.xml.fasta", "fasta")]
len(sizes), min(sizes), max(sizes)
sizes
import pylab

pylab.hist(sizes, bins=20)
pylab.title(
    "%i homologous sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
)
pylab.xlabel("Sequence length (bp)")
pylab.ylabel("Count")
pylab.show()

