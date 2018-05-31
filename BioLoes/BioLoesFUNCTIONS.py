import re


def create_codon_table():
    codontable = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    return codontable


def find_ORFs(RNA):
    RNA = RNA.upper()
    items = re.findall(r'ATG(?:(?!TAA|TAG|TGA)...)*(?:TAA|TAG|TGA)', RNA)
    return items


def transcript(DNA):
    DNA = DNA.upper()
    DNA.replace('T', 'U')


def create_other_side_DNA(DNA):
    other_side = ""
    for base in DNA:
        if base == "A":
            other_side += "T"
        elif base == "T":
            other_side += "A"
        elif base == "G":
            other_side += "C"
        elif base == "C":
            other_side += "G"
    return other_side


def create_other_side_RNA(RNA):
    RNA = create_other_side_DNA(RNA)
    RNA.replace("T", "U")


def translate_orf(orf):
    codontable = create_codon_table()
    eiwit = ""
    for i in [ orf[i:i+3] for i in range(0, len(orf), 3)]:
        eiwit += codontable[i]
    return eiwit


def create_primer(DNA, temp_or_coding="Coding", len_primer=6):
    if temp_or_coding == "Template":
        print(DNA, temp_or_coding)

    elif temp_or_coding == "Coding":
        print(DNA, temp_or_coding)
        for base in [DNA[i] for i in range(len_primer)]:
            print(base)