import BioLoes.process_fasta as process_fasta


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
        return process_fasta.process_fasta(self.fasta_data)



