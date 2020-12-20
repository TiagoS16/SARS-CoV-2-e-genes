# IMPORTS
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO

# FUNCOES

def get_prot(id):
    '''
    VARIAVEIS:
        id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    RETURNS:
        Lista de Acession numbers filtrados pelo tipo gb e sem repetições
    '''
    from Bio import ExPASy
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")
    print(seq_record.seq)
    print(len(seq_record.seq), 'aa')
    for k, v in seq_record.annotations.items():
        print(k, v)
    tam= len(seq_record.seq)
    seq= seq_record.seq
    tax= seq_record.annotations["taxonomy"]
    org= seq_record.annotations["organism"]
    #host= seq_record.annotations["organism_host"]
    y = ('ID:' + id + '|' + 'SEQUENCE:' + seq + '|' + 'SEQUENCE LENGTH:' + str(tam) + 'bp' + '|' + 'TAXONOMY:' + str(tax) + '|' + 'ORGANISM:' + org )
    return y

def filtro(seq):
    '''
    VARIAVEIS:
        seq = string resultado do get_prot(id)
    RETURNS:
        Lista da string separada pelas "|"
    '''
    seq = seq.split('|')
    return seq

def blast_prot(FILE, seq):
    '''
    VARIAVEIS:
        FILE = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        seq - sequencia proteica query para executar o blast
    RETURNS:
        Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
        do alinhamento e e-value
    '''
    result_handle = NCBIWWW.qblast('blastp', 'nr', seq)
    with open(FILE, "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

def parse(file, E_VALUE_THRESH):
    '''
    VARIAVEIS:
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitável para tratamento do output do blast.
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
    return FILE

def isol_AC(parsed_list):
    '''
    VARIAVEIS:
        parsed_list = Lista devolvida filtrada pela função parse
    RETURNS:
        Lista de Acession numbers filtrados pelo tipo gb e sem repetições.
    '''
    DicAC = {}
    for hit in parsed_list:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[0: c[0]]
        if type == "gb":
            k = hit[c[0]+1 : c[1]]
            if k not in DicAC:
                DicAC[k] = 1
    ListAC = list(DicAC.keys())
    return ListAC

def proteico(id,file,blast = False, E_VALUE_THRESH = None):
    '''
    VARIAVEIS:
        genbank = ficheiro genbank com a extensão ponto gb (ex: prot.gb)
        id = id da base de SWISS Prot da proteina a ser tratada
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        blast = Em caso de omissão recebe valor  de False, se Blast = True irá utilizar o ficheiro genbank e
        realizar um blast.
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitavel para tratamento do output do blast.
    RETURNS:
        Gera um ficheiro .txt contendo os Acession Number dos resultados do blast com filtração segundo o
        E_VALUE_THRESH e "gb".
        '''
    if blast == True:
        x = get_prot(id)
        print(x)
        seq = filtro(x)
        print(seq)
        blast_prot(file, seq[1])
    x = get_prot(id)
    print(x)
    x = parse(file, E_VALUE_THRESH)
    print(x)
    ListAC = isol_AC(x)
    print(ListAC)
    with open('id_list_prot.txt', 'w') as f:
        for item in ListAC:
            f.write("%s\n" % item)

def parse_prot(file):
    '''
    VARIAVEIS:
        file = Nome do ficheiro resultado do Blast ( ex: "FGB_blast.xml")
    RETURNS:
        Informações contidas no ficheiro impressos sobre na consola.
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



def isol_blasthit(lista):
    '''
    VARIAVEIS:
        lista = Lista devolvida filtrada pela função parse
    RETURNS:
        Ficheiro contento todos os resultados do Blast com o respetivo Acession Number | tipo | e descrição do resultado.
    '''
    DicAC = {}
    for hit in lista:
        print(hit)
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[0 : c[0]]
        y = hit[c[0] + 1: c[1]]
        descrip = hit[c[1] + 1: c[2]]
        final = y + ' | ' + type + ' | ' + descrip
        if final not in DicAC:
            DicAC[final] = 1
    ListAC = list(DicAC.keys())
    with open('blast_qresult.txt', 'w') as f:
        for i in ListAC:
            f.write("%s\n" % i)

