class BioLoesFASTA:
    def __init__(self, file):
        self.object = "BioLoes"
        self.fasta_file = file
        self.fasta_data = self.open_fasta()
        self.fasta_seq = self.process_fasta()

    def open_fasta(self):
        with open(self.fasta_file) as f:
            return f.read()

    def process_fasta(self):
        splitted_fasta = self.fasta_data.split(">")
        all_fastas = []
        for i in splitted_fasta:
            if i:
                tmp = i.split("\n")
                tmper = Fasta_object.FastaObject(tmp[0], ''.join(tmp[1:len(tmp)]), len(''.join(tmp[1:len(tmp)])))
                all_fastas.append(tmper)
        return all_fastas


