from Bio import Phylo

alignment = open('SeqsHomologas_FGG_prot_blast.xml.dnd')
tree = Phylo.read(alignment, 'newick')
Phylo.draw_ascii(tree)
tree.ladderize() # Flip branches so deeper clades are displayed at top
Phylo.draw(tree)


