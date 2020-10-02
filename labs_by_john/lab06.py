class myseq:
    """Combined Arithmetic, Geometric and fromFile sequences"""
    def __init__(self, start, qd, _type = 'arithmetic'):
        self.start = start
        self.qd = qd
        self._type = _type
        self.sequence = []
    @staticmethod
    def GeometricSequence(g, q):
        return myseq(g, q, 'geometric')
    
    @staticmethod
    def ArithmeticSequence(a, d):
        return myseq(a,d)

    def sequenceFromFile(self, file):
        rawData = []
        try:
            with open(file, 'r') as f:
                for row in f.readlines():
                    rawData.append(row)
        except FileNotFoundError:
            print("File not found.")
        if len(rawData) != 0:
            try:
                self.sequence.extend(list(map(float,rawData)))
            except ValueError:
                print("Incorrect format on file. Needs to be floats")
            
    def __getitem__(self, key):
        fileRows = len(self.sequence)

        if isinstance(key, slice):
            if key.start == -1 or key.stop == -1: raise IndexError()

            start = key.start if key.start != None else 0
            stop = key.stop
            seq = []
            if self._type == 'geometric':
                if fileRows == 0:
                    # no fileinput
                    seq = [self.start * self.qd ** n for n in range(start,stop)]

                else:
                    if start > fileRows or stop < fileRows: raise IndexError()
                    # from file
                    value = self.start
                    seq = [self.start * q ** n for n, q in enumerate(self.sequence)]
            else:
                if fileRows == 0:
                    # no fileinput
                    seq = [self.start + n * self.qd for n in range(start,stop)]

                else:
                    if start > fileRows or stop < fileRows: raise IndexError()
                    # from file
                    seq = [self.start + n * d for n, d in enumerate(self.sequence)]
            return seq

        else:
            if key == -1: raise IndexError()
            if self._type == 'geometric':
                return self.start * self.qd  ** key
            else:
                return self.start + self.qd * key


if __name__ == "__main__":
    g = myseq.GeometricSequence(5,2)
    a = myseq.ArithmeticSequence(5,2)

    print(sum(g[:10]))
    print(sum(a[:10]))

    g.sequenceFromFile('test.file') # 10 rows with 2 on each.
    a.sequenceFromFile('test.file')
    print(sum(g[:10]))
    print(sum(a[:10]))
