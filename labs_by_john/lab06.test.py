from lab06 import myseq

a = myseq.ArithmeticSequence(5,2)
g = myseq.GeometricSequence(5,2)

print(sum(a[:10]) == 140)
print(sum(g[:10]) == 5115)

g.sequenceFromFile('test.file')

print(sum(g[:10]) == 5115)