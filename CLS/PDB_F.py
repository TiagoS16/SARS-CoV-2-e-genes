from Bio.PDB import *
import pymol
class PDB:
    def __init__(self, id):
        self.id = id
    def PDB(self):
        """"
            ID: fornecer o ID da PDB
            Return: A estrutura 3D da proteína
        """
        pdbl = PDBList()
        file = pdbl.retrieve_pdb_file(self.id, pdir='.', file_format='pdb')
        pymol.finish_launching()
        pymol.cmd.load(file, self.id)
        pymol.cmd.disable("all")
        pymol.cmd.enable(self.id)
        pymol.cmd.orient()
        pymol.cmd.zoom()
        pymol.cmd.png("Protein2.png", 3000, 3000, dpi=500, ray=1)

        pymol.cmd.quit()

