class FastaObject:
    def __init__(self, title, sequence):
        self.title = title
        self.sequence = sequence
        self.length = len(sequence)
