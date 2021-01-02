from Bio.Align.Applications import ClustalwCommandline

class Mutiple:
    '''
    VARIAVEIS:
        dir = diretoria do programa clustalw2
        in_file = nome do ficheiro fasta a usar para o alinhamento
    RETURNS:
        Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
        do alinhamento e e-value
    '''
    def __ini__(self, dir, in_file):
        self.diretoria= dir
        self.in_file = in_file

    def alignment(self):
        clustalw_cline = ClustalwCommandline(self.diretoria, infile= self.in_file)
        clustalw_cline()
        print(clustalw_cline)
