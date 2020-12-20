# IMPORTS
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SearchIO


# FUNCOES
def bio_dna(ficheiro, tipo):
    '''
    ficheiro= nome e extensao do ficheiro a ler;
    tipo= extensao do ficheiro a ler (e.g. genbank);
    '''
    record = SeqIO.read(ficheiro, tipo)

    id = record.name
    tam = len(record.seq)
    seq = record.seq
    source = record.annotations["source"]
    print(' ID:', id, '\n', 'SEQUENCE LENGTH:', tam, 'bp', '\n', 'SEQUENCE:', seq, '\n', 'SOURCE:', source, '\n', 'FEATURES:')
    for i in record.features:
        print(i)


def blast_dna(ficheiro, tipo, blast):
    '''
    ficheiro= nome e extensao do ficheiro a ler;
    tipo= extensao do ficheiro a ler (e.g. gb);
    blast= nome do ficheiro incluindo a entensao .xml para guardar o resultado do blast;
    '''
    record = SeqIO.read(open(ficheiro), format=tipo)

    result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)

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


def blast_dna_pars(ficheiro):
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
#bio_dna('ORF3a.gb', 'genbank')
# blast_dna('ORF3a.gb', 'gb', 'ORF3a_blast.xml')
# blast_dna_pars('ORF3a_blast.xml')