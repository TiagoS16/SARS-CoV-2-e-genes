from Bio import Phylo

class Phylo:
    def __init__(self, nome, file):
        self.name = name
        self.file = file
    def obter_arvore(self):
        alignment = open(self.file)
        tree = Phylo.read(alignment, 'newick')
        Phylo.draw_ascii(tree)
        tree.ladderize() # Flip branches so deeper clades are displayed at top
        Phylo.draw(tree)