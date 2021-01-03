from Bio import Entrez
from Bio import SeqIO

class ID:
    def __init__(self, query, database, res, email, file_output, id = None):
        self.query = query
        self.database = database
        self.resultados = res
        self.email = email
        self.file_output = file_output
        self.id = id

    def SEARCH(self):
        print('A iniciar pesquisa...')
        Entrez.email = self.email
        li = ["FGA","FGB","FGG"]
        if self.query == 'ORF3a':
            if self.database == 'Nucleotide':
                handle = Entrez.esearch(db=self.database, sort='relevance',term='coronavirus 2' + self.query + ',RefSeq', retmax=self.resultados)
            elif self.database == 'Protein':
                handle = Entrez.esearch(db=self.database, sort='relevance',term="Coronavirus 2 " + self.query + ', RefSeq', retmax=self.resultados)
        elif self.query in li:
            if self.database == "Nucleotide":
                handle = Entrez.esearch(db=self.database, sort='relevance', term= "Homo Sapiens[ORGN] " + self.query + ', RefSeqGene', retmax=self.resultados)
            elif self.database == 'Protein':
                handle = Entrez.esearch(db=self.database, sort='relevance',term="Homo Sapiens[ORGN] " + self.query + ', RefSeq', retmax=self.resultados)
            else: print ( "ERROR")
        else:
            handle = Entrez.esearch(db=self.database, sort='relevance',term= self.query + ', RefSeqGene', retmax=self.resultados)
        record = Entrez.read(handle)
        idlist = record['IdList']
        handle.close()
        print('Id obtido = ' + idlist[0])
        self.id = idlist[0]

    def Save_file(self):
        print('A guardar ficheiro...')
        File = Entrez.efetch(db=self.database, id= self.id, retmode='text', rettype= self.file_output)
        read = SeqIO.read(File,self.file_output)
        File.close()
        name = self.query + "_" + self.database + "." + self.file_output
        SeqIO.write(read, name ,self.file_output)
        print('Ficheiro guardado segundo ' + name)


class Prot_ID:
    '''
    VARIAVEIS:
        id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    RETURNS:
       Lista de Acession numbers filtrados pelo tipo gb e sem repetições
    '''
    database = 'swiss'
    def __init__(self, id):
        self.id = id

    def get_prot(self):
        print('A iniciar pesquisa...')
        from Bio import ExPASy
        with ExPASy.get_sprot_raw(self.id) as handle:
            seq_record = SeqIO.read(handle, Prot_ID.database)
        tam = len(seq_record.seq)
        seq = seq_record.seq
        tax = seq_record.annotations["taxonomy"]
        org = seq_record.annotations["organism"]
        name = self.id + '_prot.txt'
        file = open(name, 'w+')
        file.write('> ID:' + self.id + '_'+ str(tam) + 'bp' + '_' +  str(tax) + '_' + org + '\n' + seq + '\n')
        print('Ficheiro guardado segundo ' + name)
        return seq

