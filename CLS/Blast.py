from Bio import SeqIO
from Bio.Blast import NCBIWWW

class Blast:
    def __init__(self, ficheiro , format):
        '''
        VARIAVEIS:
            Self = Acession number
            ficheiro = ficheiro <genbank ou fasta>
            format = formato do ficheiro <'gb' ou fasta>
        '''
        self.ficheiro = ficheiro
        self.format = format

    def blast_dna(self):
        '''
            VARIAVEIS:
                Self = Acession number
                ficheiro = ficheiro <genbank ou fasta>
                format = formato do ficheiro <'gb' ou fasta>
            RETURNS:
                Gera um ficheiro .xml com o resultado do blastn contra   a database dos nucleotidos .
            '''
        record = SeqIO.read(self.ficheiro, format= self.format)
        result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)
        name = self + "_blast.xml"
        with open(name, "w") as out_handle:
            out_handle.write(result_handle.read())
        result_handle.close()

    def blast_prot(self):
        '''
        VARIAVEIS:
                Self = Acession number
        RETURNS:
            Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
            do alinhamento e e-value
        '''
        record = SeqIO.read(self.ficheiro, format= self.format)
        result_handle = NCBIWWW.qblast('blastp', 'nr', record.seq)
        name = self + "_blast.xml"
        with open(name, "w") as out_handle:
            out_handle.write(result_handle.read())
        result_handle.close()