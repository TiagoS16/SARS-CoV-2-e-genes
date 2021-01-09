from Bio import Phylo

class Phylo:
    def __init__(self, nome, file):
        self.name = nome
        self.file = file
    def obter_arvore(self):
        alignment = open(self.file)
        tree = Phylo.read(alignment, 'newick')
        Phylo.draw_ascii(tree)
        tree.ladderize() # Flip branches so deeper clades are displayed at top
        Phylo.draw(tree)

        tree = tree.as_phyloxml()
        tree.ladderize()  # Flip branches so deeper clades are displayed at top
        tree.root.color = "blue"
        Phylo.draw(tree)