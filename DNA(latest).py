from Bio import Entrez
from Bio import SeqIO
from Bio import SearchIO
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW

def DNA_inf(ficheiro):
    '''
    VARIAVEIS:
        ficheiro = nome para ficheiro de extensão ponto gb (ex: prot.gb)
        type - tipo de ficheiro a ser lido (EX. GENBANK)
    RETURNS:
        Imprime informações contidas no ficheiro
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
    '''
    VARIAVEIS:
        genbank = ficheiro genbank com a extensão ponto gb (ex: prot.gb)
        blast_file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
    RETURNS:
        Gera um ficheiro .xml com o resultado do blastn contra   a database dos nucleotidos .
    '''
    record = SeqIO.read(genbank, format='gb')
    result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)
    with open(blast_file, "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

def isol_AC(lista, id):
    '''
    VARIAVEIS:
        id = id associado ao gene a ser tratado
        lista = Lista devolvida filtrada pela função obter_x
    RETURNS:
        Lista de Acession numbers filtrados pelo tipo gb e sem repetições.
    '''
    DicAC = {}
    DicAC[id] = 1
    for hit in lista:
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

def obter_lista(file, E_VALUE_THRESH):
    '''
    VARIAVEIS:
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitavel para tratamento do outpur do blast.
    RETURNS:
        Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
        do alinhamento e e-value
    '''
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
    '''
    VARIAVEIS:
        genbank = ficheiro genbank com a extensão ponto gb (ex: prot.gb)
        id = id associado ao gene a ser tratado
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        blast = Em caso de omissão recebe valor  de False, se Blast = True irá utilizar o ficheiro genbank e
        realizar um blast.
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitavel para tratamento do outpur do blast.
    RETURNS:
        Gera um ficheiro .txt contendo os Acession Number dos resultados do blast com filtração segundo o
        E_VALUE_THRESH e "gb".
    '''

    DNA_inf(genbank)
    if blast == True:
        blast_DNA(genbank, file)
    x = obter_lista(file, E_VALUE_THRESH)
    ListAC = isol_AC(x, id)
    with open('id_list_DNA.txt', 'w') as f:
        for item in ListAC:
            f.write("%s\n" % item)


def isol_blasthit(x):
    '''
    VARIAVEIS:
        x = Lista devolvida filtrada pela função obter_lista
    RETURNS:
        Ficheiro contento todos os resultados do Blast com o respetivo Acession Number | tipo | e descrição do resultado.
    '''
    DicAC = {}
    for hit in x:
        print(hit)
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[c[1]+1 : c[2]]
        y = hit[c[2]+1 : c[3]]
        descrip = hit[c[3] + 1: c[4]]
        final = y + ' | ' + type + ' | ' + descrip
        if final not in DicAC:
            DicAC[final] = 1
    ListAC = list(DicAC.keys())
    with open('blast_qresult.txt', 'w') as f:
        for i in ListAC:
            f.write("%s\n" % i)

def parse_dna(file):
    '''
    VARIAVEIS:
        file = ficheiro xml contendo os resultados de um blast
    RETURNS:
        Imprime na consola informações relativas a esse blast
    '''
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
