from Bio.Blast import NCBIXML
from Bio import SearchIO

class homologas:
    def __init__(self, ficheiro_blast, E_VALUE_THRESH = None):
        self.ficheiro = ficheiro_blast
        self.E_value = E_VALUE_THRESH
        if self.E_value == None :
            self.E_value = 0.05

    def File_hits(self):
        '''
        VARIAVEIS:
            self = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
            E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
            aceitavel para tratamento do output do blast.
        RETURNS:
            Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
            do alinhamento e e-value
        '''
        result_handle = open(self.ficheiro)
        blast_record = NCBIXML.read(result_handle)
        AC = self.ficheiro.split('_')
        FILE = str('SeqsHomo_' + str(AC[0]) + '.fasta')
        FILE2 = str('ACHomo_' + str(AC[0]) + '.txt')
        ficheiro_output = open(FILE, 'w+')
        ficheiro_output2 = open(FILE2, 'w+')
        D = {}
        for alignment in blast_record.alignments:
            for i in range(len(alignment.hsps)):
                hsp = alignment.hsps[i]
                if hsp.expect < self.E_value:
                    if hsp != 0:
                        ficheiro_output.write('>' + alignment.hit_id + '_' + str(hsp.expect) + '\n' + alignment.hsps[i].sbjct + '\n')
                        if alignment.accession not in D:
                            D[alignment.accession] = 0
                            ficheiro_output2.write(alignment.accession + '\n')
                    else:
                        ficheiro_output.write('>' + alignment.hit_id + '_' + str(hsp.expect) + '\n' + alignment.hsps[i].sbjct + '\n')
        result_handle.close()
        ficheiro_output.close()
        ficheiro_output2.close()

    def BLAST_REPORT(self):
        result_handle = open(self.ficheiro)
        blast_record = NCBIXML.read(result_handle)
        AC = self.ficheiro.split('_')
        FILE = str('Report_' + str(AC[0]) + '.fasta')
        ficheiro_output = open(FILE, 'w+')
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < self.E_value:
                    N = ("****Alignment****" + '\n' + "sequence:" + alignment.title + '\n' + "length:" + str(alignment.length) + '\n' + "e value:" + str(hsp.expect) +'\n' + '\n')
                    ficheiro_output.write(N)
        blast_qresult = SearchIO.read(self.ficheiro, "blast-xml")
        ficheiro_output.write(str(blast_qresult))
