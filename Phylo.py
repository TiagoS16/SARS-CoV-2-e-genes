from Bio import Phylo

alignment = open('SeqsHomologas_FGG_blast.xml.dnd')
tree = Phylo.read(alignment, 'newick')
Phylo.draw_ascii(tree)
