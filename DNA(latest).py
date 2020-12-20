from Bio import Entrez
from Bio import SeqIO
from Bio import SearchIO
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW

def bio_dna(ficheiro):
    '''
    ficheiro = nome para ficheiro de extensão ponto gb (ex: prot.gb) ;
    '''
    record = SeqIO.read(ficheiro, 'genbank')
    id = record.name
    tam = len(record.seq)
    seq = record.seq
    source = record.annotations["source"]
    print(' ID:', id, '\n', 'SEQUENCE LENGTH:', tam, 'bp', '\n', 'SEQUENCE:', seq, '\n', 'SOURCE:', source, '\n', 'FEATURES:')
    for i in record.features:
        print(i)

def blast_DNA(genbank, blast_file):
    record = SeqIO.read(genbank, format='gb')
    result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)
    with open(blast_file, "w") as out_handle:
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

def DNA(genbank, id, file,blast = False, E_VALUE_THRESH = None):
    bio_dna(genbank)
    if blast == True:
        blast_DNA(genbank, file)
    x = obter_x(file, E_VALUE_THRESH)
    ListAC = isol_AC(x, id)
    with open('id_list_DNA.txt', 'w') as f:
        for item in ListAC:
            f.write("%s\n" % item)

DNA('FGG.gb','NC_000004.12', 'FGG_blast.xml', False, None)

def parse_dna(file):
    result_handle = open(file)
    from Bio.Blast import NCBIXML
    blast_record = NCBIXML.read(result_handle)
    E_VALUE_THRESH = 0.04
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")
    from Bio import SearchIO
    blast_qresult = SearchIO.read(file, "blast-xml")
    print(blast_qresult)
    result_handle.close()

parse_dna('FGG_blast.xml')