class BioLoesSEQ:
    def __init__(self, sequence, type_DNA=""):
        self.sequence = sequence.upper()
        self.type_DNA = type_DNA

    def __str__(self):
        return "SEQ object with sequence %s" % self.sequence

    def __len__(self):
        return len(self.sequence)

    def reverse_sequence(self):
        return self.sequence[::-1]

    def upper(self):
        return self.sequence.upper()

    def lower(self):
        return self.sequence.lower()

    def get_complement(self):
        complement = ""
        for i in self.sequence:
            if i == "A":
                complement += "T"
            elif i == "T":
                complement += "A"
            elif i == "G":
                complement += "C"
            elif i == "C":
                complement += "G"
        return complement

    def get_reversed_complement(self):
        return self.get_complement()[::-1]

    def GC_content(self):
        G_count = self.sequence.count("G")
        C_count = self.sequence.count("C")
        GC_content = (G_count + C_count)/len(self.sequence)
        return GC_content

    def translate_to_RNA(self):
        mRNA = ""
        for i in self.sequence:
            if i == "T":
                mRNA += "U"
            else:
                mRNA += i
