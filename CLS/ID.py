from Bio import Entrez
from Bio import SeqIO

class ID:
    def __init__(self, query, database, res, email, file_output):
        self.query = query
        self.database = database
        self.resultados = res
        self.email = email
        self.file_output = file_output

    def SEARCH(self):
        Entrez.email = self.email
        if self.query == "FGA" or "FGB" or "FGG":
            if self.database == "nucleotide":
                handle = Entrez.esearch(db=self.database, sort='relevance', term= "Homo Sapiens[ORGN] " + self.query + ', RefSeqGene', retmax=self.resultados)
            elif self.database == 'protein':
                handle = Entrez.esearch(db=self.database, sort='relevance',term="Homo Sapiens[ORGN] " + self.query + ', RefSeq', retmax=self.resultados)
            else: print ( "ERROR")

        elif self.query == "ORF3a":
            if self.database == "nucleotide":
                handle = Entrez.esearch(db=self.database, sort='relevance',term="Corona virus 2 " + self.query + ', RefSeq', retmax=self.resultados)
            elif self.database == 'protein':
                handle = Entrez.esearch(db=self.database, sort='relevance',term="Coronavirus 2 " + self.query + ', RefSeq', retmax=self.resultados)
        else:
            handle = Entrez.esearch(db=self.database, sort='relevance',term= self.query + ', RefSeqGene', retmax=self.resultados)
        record = Entrez.read(handle)
        idlist = record['IdList']
        print(idlist)
        handle.close()
        return idlist[0]

    def Save_file(self):
        id_gene = ID.SEARCH(self)
        File = Entrez.efetch(db=self.database, id=id_gene, retmode='text', rettype=self.file_output)
        read = SeqIO.read(File,self.file_output)
        File.close()
        name = self.query + "_" + self.database + "_" + self.file_output + ".txt"
        print(name)
        SeqIO.write(read, name ,self.file_output)


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
        return seq
