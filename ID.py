from Bio import Entrez
from Bio import SeqIO
from Bio import Medline

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
        name = self.id + '_prot.fasta'
        file = open(name, 'w+')
        file.write('>ID:' + self.id + '_'+ str(tam) + 'bp' + '_' +  str(tax) + '_' + org + '\n' + str(seq) + '\n')
        print('Ficheiro guardado segundo ' + name)

class Get_info:
    def __init__(self, genbank):
        self.gen = genbank

    def gb_inf(self):
        record = SeqIO.read(self.gen, 'genbank')
        id = record.name
        tam = len(record.seq)
        seq = record.seq
        source = record.annotations["source"]
        print(' ID:', id, '\n', 'SEQUENCE LENGTH:', tam, 'bp', '\n', 'SEQUENCE:', seq, '\n', 'SOURCE:', source, '\n',
              'FEATURES:')
        for i in record.features:
            print(i)


class Pubmed:
    def __init__(self,nome, query, res):
        self.query = query
        self.name = nome
        self.res = res

    def procura(self):
        Entrez.email = 'example@gmail.com'
        handle = Entrez.esearch(db='Pubmed', sort='relevance', term=self.query, retmax=self.res)
        record = Entrez.read(handle)
        handle.close()
        idlist = record['IdList']
        handle = Entrez.efetch(db= 'Pubmed', id=idlist, rettype="medline", retmode="text")
        records = Medline.parse(handle)
        FILE = str('Pubmed_' + self.name + '.txt')
        ficheiro_output = open(FILE, 'w+')
        print('A guardar ficheiro...')
        for record in records:
            x = ">Title: " + str(record.get("TI", "?")) + '\n' +'>Abstract: ' + str(record.get('AB', '?')) + '\n' + ">Authors: " + str(record.get("AU", "?")) + '\n' + ">Source: " + str(record.get("SO", "?")) + '\n' + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'+'\n'
            ficheiro_output.write(x)
        print('ficheiro guardado segundo: ' + FILE)

