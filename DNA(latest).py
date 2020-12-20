from Bio import Entrez
from Bio import SeqIO
from Bio import SearchIO
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW

def blast_DNA(FILE):
    record = SeqIO.read(open(FILE), format='gb')
    result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)
    with open(FILE, "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

def isol_AC(x, id):
    DicAC = {}
    DicAC[id] = 1
    for hit in x:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[c[1]+1 : c[2]]
        if type == "gb":
            y = hit[c[2]+1 : c[3]]
            if y not in DicAC:
                DicAC[y] = 1
    ListAC = list(DicAC.keys())
    return ListAC

def obter_x(file, E_VALUE_THRESH):
    result_handle = open(file)
    blast_record = NCBIXML.read(result_handle)
    FILE = []
    if E_VALUE_THRESH == None:
        E_VALUE_THRESH = 0.05
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                y = alignment.title + '|' + str(alignment.length) + '|' + str(hsp.expect)
                FILE.append(y)
    result_handle.close()
    return FILE

def DNA(id,file,blast = False, E_VALUE_THRESH = None):
    if blast == True:
        Start = input("introduzir nome do ficheiro GenBank")
        blast_DNA(Start)
    x = obter_x(file, E_VALUE_THRESH)
    ListAC = isol_AC(x, id)
    with open('id_list_DNA.txt', 'w') as f:
        for item in ListAC:
            f.write("%s\n" % item)

DNA('NC_000004.12', 'FBB_blast.xml', False, None)
