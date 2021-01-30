from Bio import Entrez
from Bio import SeqIO

word = 'FGB[Gene]'
res= 1
email= 'pg42877@alunos.uminho.pt'
Entrez.email= email
handle = Entrez.esearch(db = 'nucleotide', term=word, retmax= res)
record = Entrez.read(handle)
gi_list = record['IdList']
print(gi_list)

for a in gi_list:
    a = 'NG_008833.1'
    handle = Entrez.efetch(db="nucleotide", id=a, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    save_file = open('my_blast.xml', 'w')
    save_file.write(handle.read())
    handle.close()
    print(record.id)
