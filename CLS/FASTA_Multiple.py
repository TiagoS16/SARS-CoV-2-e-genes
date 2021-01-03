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
    def __init__(self, name, file, database):
        self.file = file
        self.name = name
        self.db = database

    def m_blast(self):
        print('A criar ficheiro...')
        Output = self.name + 'fullhomo_AC.fasta'
        ficheiro_output = open(Output, 'w+')
        ficheiro = open(self.file, 'r')
        b_file = ficheiro.readlines()
        print('A recolher informações...')
        for a in b_file:
            Entrez.email = 'example@gmail.com'
            File = Entrez.efetch(db= self.db, id= a, retmode='text', rettype= 'fasta')
            read = SeqIO.read(File, 'fasta')
            File.close()
            ficheiro_output.write('>' + a + str(read.seq) + '\n' + '\n')
        print('Ficheiro gravado sobre o nome ' + Output)
