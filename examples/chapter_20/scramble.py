"""
Generator Functions and Expressions
Generating Scrambled Sequences

- Generator function
- Generator expression
- Tester client
"""


# Generator function
def scramble(seq):
    for i in range((len(seq))):
        yield seq[1:] + seq[:1]


print(list(scramble("test")))
print(list(scramble([1, 2, 3])))
print(list(scramble((1, 2, 3))))


# Generator expressions
S = 'spam'

G = (S[i:] + S[:i] for i in range(len(S)))
print(list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print(list(F(S)))

