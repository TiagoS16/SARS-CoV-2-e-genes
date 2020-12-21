from Bio.PDB import *
import pymol
def PDB(ID):
    """"
    ID: fornecer o ID da PDB
    Return: A estrutura 3D da proteína
    """
    pdbl = PDBList()
    file = pdbl.retrieve_pdb_file(ID, pdir='.', file_format='pdb')
    pymol.finish_launching()

    pymol.cmd.load(file, ID)
    pymol.cmd.disable("all")
    pymol.cmd.enable(ID)
    pymol.cmd.zoom()
    pymol.cmd.png("Protein2.png", 3000, 3000, dpi=500, ray=1)

    pymol.cmd.quit()

