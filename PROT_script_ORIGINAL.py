# IMPORTS
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO



# FUNCOES
def get_prot(id):
    '''
    id= codigo da poteina a pesquisar na base de dados Swiss-Prot;
    '''
    from Bio import ExPASy
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")

    tam= len(seq_record.seq)
    seq= seq_record.seq
    fun= seq_record.annotations["comment"]
    tax= seq_record.annotations["taxonomy"]
    org= seq_record.annotations["organism"]
    print(' ID:', id, '\n', 'SEQUENCE LENGTH:', tam, 'bp', '\n', 'SEQUENCE:', seq, '\n', 'TAXONOMY:', tax, '\n', 'ORGANISM:', org, '\n', fun)

'''
    if t == TRUE:
        print(' ID:', id, '\n', 'SEQUENCE LENGTH:', tam, 'bp', '\n', 'SEQUENCE:', seq, '\n', 'TAXONOMY:', tax, '\n', 'ORGANISM:', org, '\n', 'ORGANISM HOST:', host, '\n', fun)
    else:
        return seq
'''

def blast_prot(id, blast):
    '''
    id= codigo da proteina a pesquisar na base de dados Swiss-Prot;
    blast= nome do ficheiro incluindo a entensao .xml para guardar o resultado do blast;
    '''

    from Bio import ExPASy
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")

    seq_prot= seq_record.seq

    result_handle = NCBIWWW.qblast('blastp', 'nr', seq_prot)

    with open(blast, "w") as out_handle:
        out_handle.write(result_handle.read())

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

    blast_qresult = SearchIO.read(blast, "blast-xml")
    print(blast_qresult)

    blast_hit = blast_qresult[0]  # first hit from the query result
    print(blast_hit)

    result_handle.close()


def blast_prot_pars(ficheiro):
    '''
    ficheiro= nome e extensao do ficheiro a ler;
    '''
    result_handle = open(ficheiro)

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

    blast_qresult = SearchIO.read(ficheiro, "blast-xml")
    print(blast_qresult)

    blast_hit = blast_qresult[0]  # first hit from the query result
    print(blast_hit)



# CHAMADAS
# get_prot('P0DTC3')
# blast_prot('P0DTC3', "PROT_ORF3a_blast1.xml")
# blast_prot_pars("PROT_ORF3a_blast.xml")