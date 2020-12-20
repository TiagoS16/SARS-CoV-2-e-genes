# IMPORTS
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO

# FUNCOES

def get_prot(id, imprimir = False):
    '''
    id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    '''
    from Bio import ExPASy
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")
    tam= len(seq_record.seq)
    seq= seq_record.seq
    fun= seq_record.annotations["comment"]
    tax= seq_record.annotations["taxonomy"]
    org= seq_record.annotations["organism"]
    #host= seq_record.annotations["organism_host"]
    y = (' ID:' + id + '|' + 'SEQUENCE:' + seq + '|' + 'SEQUENCE LENGTH:' + str(tam) + 'bp' + '|' + 'TAXONOMY:' + str(tax) + '|' + 'ORGANISM:' + org + '|' + fun)
    if imprimir == True:
        print(y)
    return y

def filtro(seq):
    seq = seq.split('|')
    return seq


def blast_prot(FILE, seq):
    '''
    id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    blast= nome do ficheiro incluindo a entensao .xml para guardar o resultado do blast;
    '''
    result_handle = NCBIWWW.qblast('blastp', 'nr', seq)
    with open(FILE, "w") as out_handle:
        out_handle.write(result_handle.read())

def parse(file, imprimir, E_VALUE_THRESH):
    result_handle = open(file)
    blast_record = NCBIXML.read(result_handle)
    FILE = []
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
    return FILE

def isol_AC(x, id):
    ListAC = [id, ]
    for hit in x:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        ListAC.append(hit[c[1]+1 : c[2]])
    return ListAC

def proteico(id,blast = False, imprimir, file, E_VALUE_THRESH):
    if blast = True:
        x = get_prot(id, imprimir)
        seq = filtro(x)
        blast_prot(file, seq[1])
    else:
        x = parse(file, E_VALUE_THRESH)
        ListAC = isol_AC(x, id)




# CHAMADAS
# bio_prot('ORF3a.gb', 'genbank')
# blast_prot('ORF3a.gb', 'gb', 'ORF3a_blast.xml')
# blast_prot_pars('ORF3a_blast.xml')
# get_prot('P02675', True)
#blast_prot('P0DTC3', "PROT_ORF3a_blast1.xml")
#blast_prot_pars("PROT_ORF3a_blast.xml")
#yo
