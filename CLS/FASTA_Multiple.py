from Bio import Entrez
from Bio import SeqIO

class Create_fasta:
    '''
    VARIAVEIS:
        file = ficheiro com o conjuntos dos ACnumbers
        output = ficheiro que irá ser gerado com as variadas sequencias ('*nome*.fasta')
        database = base dados onde é procurado o resultado dos AC ('Nucleotide' ou 'Protein')
    RETURNS:
        devolve o ficheiro output gravado na diretoria com as sequencias compiladas
    '''
    def __init__(self, file, output, database):
        self.file = file
        self.output = output
        self.db = database

    def m_blast(self):
        ficheiro_output = open(self.output, 'w+')
        ficheiro = open(self.file, 'r')
        b_file = ficheiro.readlines()
        for a in b_file:
            Entrez.email = 'example@gmail.com'
            File = Entrez.efetch(db= self.db, id= a, retmode='text', rettype= 'fasta')
            read = SeqIO.read(File, 'fasta')
            File.close()
            ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')

