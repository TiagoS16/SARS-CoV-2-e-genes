from Bio.Align.Applications import ClustalwCommandline

diretoria = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
in_file = r'C:\Users\16tia\Desktop\sequence.fasta'

clustalw_cline = ClustalwCommandline(diretoria, infile=in_file)
clustalw_cline()
print(clustalw_cline)