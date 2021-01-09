from Bio import Phylo

alignment = open('entrez_prot.dnd')
tree = Phylo.read(alignment, 'newick')
tree.ladderize()
Phylo.draw_ascii(tree)

tree = tree.as_phyloxml()
tree.ladderize() # Flip branches so deeper clades are displayed at top
tree.root.color = "blue"
Phylo.draw(tree)
#Phylo.draw(tree, branch_labels=lambda c: c.branch_length)