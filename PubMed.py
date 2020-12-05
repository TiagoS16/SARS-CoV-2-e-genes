from Bio import Entrez
database = input('database: ')
word = input('query a procurar: ')
res= int(input('resultados maximos: '))
email= input('email a inserir: ')
Entrez.email= email
handle=Entrez.esearch(db = database, term=word, retmax= res)
record=Entrez.read(handle)
handle.close()
idlist= record['IdList']

from Bio import Medline

handle = Entrez.efetch(db=database, id=idlist, rettype="medline", retmode="text")
records = Medline.parse(handle)

print()

for record in records:
    print("title:", record.get("TI", "?"))
    print("authors:", record.get("AU", "?"))
    print("source:", record.get("SO", "?"))
    print("")
