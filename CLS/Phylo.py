class Phylo:
    def __init__(self, file):
        self.file = file

    def obter_arvore(self):
        from Bio import Phylo
        alignment = open(self.file)
        tree = Phylo.read(alignment, 'newick')
        Phylo.draw_ascii(tree)
        tree.ladderize() # Flip branches so deeper clades are displayed at top

        tree = tree.as_phyloxml()
        tree.ladderize()  # Flip branches so deeper clades are displayed at top
        tree.root.color = "blue"
        Phylo.draw(tree)
