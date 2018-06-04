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


def make_ds(DNA):
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


def make_dr(RNA):
    RNA = make_ds(RNA)
    RNA = RNA.replace("T", "U")
    return RNA


def translate_orf(orf):
    codontable = create_codon_table()
    eiwit = ""
    for i in [orf[i:i+3] for i in range(0, len(orf), 3)]:
        eiwit += codontable[i]
    return eiwit


def create_primer(DNA, temp_or_coding="Coding", len_primer=6):
    """
    This function will always return the DNA in the 5' to 3' direction
    """
    if temp_or_coding == "Template":
        tmp = DNA[0:len_primer]
        tmp = make_ds(tmp)
        return tmp
    elif temp_or_coding == "Coding":
        tmp = DNA[0:len_primer]
<<<<<<< HEAD
        tmp = make_ds(tmp)
        return tmp[::-1]


def is_palindromic(DNA):
    reversed_DNA = make_ds(DNA[::-1])
    for i, nc in enumerate(DNA):
        if nc != reversed_DNA[i]:
            return False
        else:
            continue
    return True
=======
        tmp = create_other_side_DNA(tmp)
        return tmp[::-1]


def is_palindrome(DNA):
    pass
>>>>>>> ca1ab959cdbf3054e05c30cac5bdfba7033a7d69
