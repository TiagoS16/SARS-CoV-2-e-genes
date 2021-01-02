from Bio import Entrez
from Bio import SeqIO

class Create_fasta:
    def __init__(self, file, output):
        self.file = file
        self.output = output

    def m_blast(self):
        ficheiro_output = open(self.output, 'w+')
        ficheiro = open(self.file, 'r')
        b_file = ficheiro.readlines()
        for a in b_file:
            Entrez.email = 'example@gmail.com'
            File = Entrez.efetch(db= 'nucleotide', id= a, retmode='text', rettype= 'fasta')
            read = SeqIO.read(File, 'fasta')
            File.close()
            ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')

test = Create_fasta('ACHomo_FBB.txt', 'Multiple.txt')
Create_fasta.m_blast(test)