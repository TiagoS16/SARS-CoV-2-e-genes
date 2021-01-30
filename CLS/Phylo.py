

class Phylo:
    def __init__(self, file):
        self.file = file

    def obter_arvore(self):
        from Bio import Phylo
        import matplotlib.pyplot as plt
        alignment = open(self.file)
        tree = Phylo.read(alignment, 'newick')
        Phylo.draw_ascii(tree)
        tree.ladderize() # Flip branches so deeper clades are displayed at top
        SMALL_SIZE = 5
        MEDIUM_SIZE = 8
        BIGGER_SIZE = 11
        plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
        plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
        plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)
        tree = tree.as_phyloxml()
        tree.ladderize()  # Flip branches so deeper clades are displayed at top
        tree.root.color = "blue"
        Phylo.draw(tree)
