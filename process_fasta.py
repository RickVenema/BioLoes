import BioLoes.Fasta_object as Fasta_object


def process_fasta(fast_file_content):
    splitted_fasta = fast_file_content.split(">")
    all_fastas = []
    for i in splitted_fasta:
        if i:
            tmp = i.split("\n")
            tmper = Fasta_object.FastaObject(tmp[0], ''.join(tmp[1:len(tmp)]), len(''.join(tmp[1:len(tmp)])))
            all_fastas.append(tmper)
    return all_fastas
