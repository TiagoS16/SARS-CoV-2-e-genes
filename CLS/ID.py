from Bio import Entrez
from Bio import SeqIO

class ID:
    def __init__(self, query, Orgn, database, res, email, file_output):
        self.query = query
        self.Orgn = Orgn
        self.database = database
        self.resultados = res
        self.email = email
        self.file_output = file_output

    def SEARCH(self):
        Entrez.email = self.email
        handle = Entrez.esearch(db=self.database, sort='relevance', term= self.Orgn + self.query + ', RefSeq', retmax=self.resultados)
        #Refseq para ORF3, corona virus 2
        #RefSeqGene para FGA,FGB,FGG
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

teste = DNA_ID('ORF3a','SARS-CoV-2','protein',10,'pg42877@alunos,uminho.pt','fasta')
DNA_ID.Save_file(teste)


# db = 'protein', para seqs de proteina de FGA,FGB,FGG; ORGN = Homo Sapiens [Orgn]
# db = 'protein', para seqs de proteina de ORF3a; ORGN = Coronavirus 2
# db = 'Nucleotide' para seqs de DNA de FGA,FGB,FGG; ORGN = Homo Sapiens [Orgn]
# db = 'Nucleotide' para seqs de DNA da ORF3a; ORGN = Corona virus 2
