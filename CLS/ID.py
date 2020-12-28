from Bio import Entrez
from Bio import SeqIO

class DNA_ID:
    def __init__(self, query, database, res, email, file_output):
        self.query = query
        self.database = database
        self.resultados = res
        self.email = email
        self.file_output = file_output

    def DNA(self):
        Entrez.email = self.email
        handle = Entrez.esearch(db=self.database, sort='revelance', term='Homo Sapiens[Orgn] AND '+ self.query + '[Gene]', retmax=self.resultados)
        record = Entrez.read(handle)
        idlist = record['IdList']
        handle.close()
        return idlist[0]

    def Save_file(self):
        id_gene = DNA_ID.DNA(self)
        File = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype=self.file_output)
        read = SeqIO.read(file,self.file_output)
        File.close()
        name = id_gene + "_gene." + self.file_output
        SeqIO.write(read, name ,self.file_output)



class Prot_ID:
    '''
    VARIAVEIS:
        id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    RETURNS:
       Lista de Acession numbers filtrados pelo tipo gb e sem repetições
    '''
    def __init__(self, id):
        self.id = id
        self.database = 'swiss'

    def get_prot(self):
        from Bio import ExPASy
        with ExPASy.get_sprot_raw(self.id) as handle:
            seq_record = SeqIO.read(handle, self.database)
        tam = len(seq_record.seq)
        seq = seq_record.seq
        tax = seq_record.annotations["taxonomy"]
        org = seq_record.annotations["organism"]
        name = self.id + '_prot.txt'
        file = open(name, 'w+')
        file.write('> ID:' + self.id + '_'+ str(tam) + 'bp' + '_' +  str(tax) + '_' + org + '\n' + seq + '\n')
        return seq