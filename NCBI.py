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

