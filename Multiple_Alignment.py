from Bio.Align.Applications import ClustalwCommandline

diretoria = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
in_file = r'entrez_prot.fasta'

clustalw_cline = ClustalwCommandline(diretoria, infile=in_file)
clustalw_cline()
print(clustalw_cline)
