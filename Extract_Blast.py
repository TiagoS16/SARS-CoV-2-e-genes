from Bio import Entrez
from Bio import SeqIO
from Bio import SearchIO

def isol_AC(x):
    ListAC = []
    for hit in x:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[c[1]+1 : c[2]]

        ListAC.append(hit[c[2]+1 : c[3]])
    return ListAC

def obter_lista(file):
    FILE = []
    DESC = []
    blast_qresult = SearchIO.read(file, "blast-xml")
    print(blast_qresult)
    for blast_hit in blast_qresult: #Get lista de IDs
        FILE.append(blast_hit.id)
    for blast_hit in blast_qresult:  # Get lista de IDs
        DESC.append(blast_hit.description)
    return FILE

def create_ac_list(file, id):
    ID_List = obter_lista(file)
    ListAC = isol_AC(ID_List)
    ListAC.append(id)
    print(ListAC)
    with open('listfile.txt', 'w') as filehandle:
        for listitem in ListAC:
            filehandle.write('%s\n' % listitem)

create_ac_list('FBB_blast.xml', 'NC_000004.12')