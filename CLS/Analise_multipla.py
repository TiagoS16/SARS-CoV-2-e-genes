from Bio import AlignIO
from Bio import SeqIO

class Align:
    def __init__(self, nome, file):
        self.nome = nome
        self.file = file

    def summary_alinhamento(self):
        name = self.nome + '_sumali.txt'
        ficheiro_output = open(name, 'w+')
        align = AlignIO.read(self.file, "clustal")
        ficheiro_output.write(align)
        ficheiro_output.write("Number of rows: %i" % len(align))
        for record in align:
            ficheiro_output.write("%s - %s" % (record.seq, record.id))
        print('Ficheiro guardado sobre o nome ' + name)

    def table_alinhamento(self):
        name = self.nome + '_tabali.txt'
        ficheiro_output = open(name, 'w+')
        align = AlignIO.read(self.file, "clustal")
        substitutions = align.substitutions
        ficheiro_output(substitutions)
        print('Ficheiro guardado sobre o nome ' + name)
# how often letters in the alignment are substituted for each other

class hist:
    def __init__(self, file):
        self.file = file

    def histogram(self):
        sizes = [len(rec) for rec in SeqIO.parse( self.file , "fasta")]
        len(sizes), min(sizes), max(sizes)
        sizes
        import pylab
        pylab.hist(sizes, bins=20)
        pylab.title("%i homologous sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes)))
        pylab.xlabel("Sequence length (bp)")
        pylab.ylabel("Count")
        pylab.show()