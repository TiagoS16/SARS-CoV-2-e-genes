import vcf
from tabulate import tabulate
from gtfparse import read_gtf


print('Spanish SARS-CoV2 variants: ')
vcf_reader = vcf.Reader(open("ERR4395294_paired.raw.vcf", "r"))
for record in vcf_reader:
    print(record)

print('--------------------------------------------------------------------')

print('Portuguese SARS-CoV2 variants: ')
vcf_reader = vcf.Reader(open("ERR4157959_paired.raw.vcf", "r"))
for record in vcf_reader:
    print(record)


# returns GTF with essential columns such as "feature", "seqname", "start", "end"
# alongside the names of any optional keys which appeared in the attribute column
df = read_gtf("Sars_cov_2.ASM985889v3.101.gtf")
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

# filter DataFrame to gene entries on chrY
df_genes = df[df["gene_name"] == "ORF3a"]
print(tabulate(df_genes, headers = 'keys', tablefmt = 'psql'))
