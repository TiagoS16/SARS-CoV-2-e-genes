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
    ListAC = [id, ]
    for hit in x:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[c[1]+1 : c[2]]
        if type == "gb":
            ListAC.append(hit[c[2]+1 : c[3]])
    return ListAC

def obter_x(file, E_VALUE_THRESH, imprimir= False):
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
            else : pass
            if imprimir == True:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")
                blast_qresult = SearchIO.read(file, "blast-xml")
                print(blast_qresult)
                blast_hit = blast_qresult[0]  # first hit from the query result
                print(blast_hit)
                result_handle.close()
    result_handle.close()
    return FILE

def DNA(id,file,blast = False, imprimir = False,  E_VALUE_THRESH = None):
    if blast == True:
        blast_DNA(file)
    else:
        x = obter_x(file, imprimir, E_VALUE_THRESH)
        ListAC = isol_AC(x, id)
        ListAC.append(id)
        with open('id_list.txt', 'w') as f:
            for item in ListAC:
                f.write("%s\n" % item)

DNA('NC_000004.12', 'FBB_blast.xml')