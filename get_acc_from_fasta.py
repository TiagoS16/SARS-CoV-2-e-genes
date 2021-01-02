#from Bio.ExPASy import ScanProsite
#handle = ScanProsite.scan(seq=sequence)

from Bio import SeqIO

def get_acc(identifier):
    """"Given a SeqRecord identifier string, return the accession number as a string.

    e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "Z78488.1"
    """
    parts = identifier.split("|")
    assert len(parts) == 5 and parts[0] == "gi"
    return parts[3]

dict = SeqIO.to_dict(SeqIO.parse("SeqsHomologas_FGG_DNA_blast.xml.fasta", "fasta"))
print(dict.keys())
accession_list = dict.keys()
result = []
for acession in accession_list:
    result.append(get_acc(acession))
with open('id_list_DNA.txt', 'w') as f:
    for item in result:
        f.write("%s\n" % item)
    f.close()
