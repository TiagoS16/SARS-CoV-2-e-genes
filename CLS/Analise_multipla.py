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
        x =align
        ficheiro_output.write(str(x) + '\n')
        ficheiro_output.write("Number of rows: %i" % len(align) + '\n')
        for record in align:
            X = "%s - %s" % (record.seq, str(record.id))
            ficheiro_output.write(X + '\n')
        print('Ficheiro guardado sobre o nome ' + name)

    def table_alinhamento(self):
        name = self.nome + '_tabali.txt'
        ficheiro_output = open(name, 'w+')
        align = AlignIO.read(self.file, "clustal")
        substitutions = align.substitutions
        D = ['#',]
        for record in align:
            for j in record.seq:
                if j not in D and j != '-':
                    D.append(j)
        D = sorted(D)
        print(D)
        for i in range(0, len(substitutions)+1):
            Y = [f'{x:9}' for x in D[i]]
            for l in Y:
                ficheiro_output.write(l)
        for i in range(0, len(substitutions)):
            ficheiro_output.write('\n')
            ficheiro_output.write(D[i + 1])
            X = [f'{x:9}' for x in substitutions[i]]
            for k in X:
                ficheiro_output.write(k)
        print('Ficheiro guardado sobre o nome ' + name)


class hist:
    def __init__(self, file):
        self.file = file

    def histogram(self):
        print('Iniciar processo...')
        sizes = [len(rec) for rec in SeqIO.parse( self.file , "fasta")]
        len(sizes), min(sizes), max(sizes)
        sizes
        import pylab
        pylab.hist(sizes, bins=20)
        pylab.title("%i homologous sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes)))
        pylab.xlabel("Sequence length (bp)")
        pylab.ylabel("Count")
        pylab.show()
        print('Plot criado')

random = Align('fodinhas2', "FGB_fullseqs_AC.aln")
Align.table_alinhamento(random)
