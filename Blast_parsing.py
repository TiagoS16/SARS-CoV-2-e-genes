result_handle = open("FBB_blast.xml")

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
         if hsp.expect < E_VALUE_THRESH:
             print("****Alignment****")
             print("sequence:", alignment.title)
             print("length:", alignment.length)
             print("e value:", hsp.expect)
             print(hsp.query[0:75] + "...")
             print(hsp.match[0:75] + "...")
             print(hsp.sbjct[0:75] + "...")



from Bio import SearchIO
blast_qresult = SearchIO.read("FBB_blast.xml", "blast-xml")
print(blast_qresult)

for blast_hit in blast_qresult: #Get lista de IDs
    print(blast_hit.id)
    print(blast_hit.description)

blast_hit = blast_qresult[0]    # first hit from the query result
print(blast_hit)

