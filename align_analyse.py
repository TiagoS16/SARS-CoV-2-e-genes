from Bio import AlignIO
align = AlignIO.read("SeqsHomologas_FGG_prot_blast.xml.aln", "clustal")
print(align)
print("Number of rows: %i" % len(align))

for record in align:
    print("%s - %s" % (record.seq, record.id))

# how often letters in the alignment are substituted for each other
substitutions = align.substitutions
print(substitutions)