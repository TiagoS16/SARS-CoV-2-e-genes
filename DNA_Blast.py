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

def obter_homologos(file, E_VALUE_THRESH):
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
    FILE = str('SeqsHomologas_' + str(file) + '.fasta')
    ficheiro_output = open(FILE, 'w+')
    if E_VALUE_THRESH == None:
        E_VALUE_THRESH = 0.05
    for alignment in blast_record.alignments:
        for hsp in range(len(alignment.hsps)):
            if alignment.hsps[hsp].expect < E_VALUE_THRESH:
                if hsp != 0:
                    ficheiro_output.write('>'+alignment.hit_id+'_'+str(hsp)+'\n'+alignment.hsps[hsp].sbjct+'\n')
                else:
                    ficheiro_output.write('>'+alignment.hit_id+'\n'+alignment.hsps[hsp].sbjct+'\n')
    result_handle.close()


def parse_dna(file,  E_VALUE_THRESH):
    '''
    VARIAVEIS:
        file = ficheiro xml contendo os resultados de um blast
    RETURNS:
        Imprime na consola informações relativas a esse blast
    '''
    result_handle = open(file)
    from Bio.Blast import NCBIXML
    blast_record = NCBIXML.read(result_handle)
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

def DNA(genbank, file,blast = False, E_VALUE_THRESH = None):
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
    obter_homologos(file, E_VALUE_THRESH)
    parse_dna(file, E_VALUE_THRESH)


DNA('FGG.gb', 'FGG_blast.xml', False, 0.05)