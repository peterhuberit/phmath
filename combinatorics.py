"""
@author Peter Huber 
https://github.com/peterhuberit/phmath
"""

# Combinatorics is an area of mathematics primarily concerned with counting, 
# both as a means and an end in obtaining results, and certain properties of 
# finite structures. It is closely related to many other areas of mathematics 
# and has many applications ranging from logic to statistical physics, from 
# evolutionary biology to computer science, etc. 

# https://en.wikipedia.org/wiki/Combinatorics
# https://hu.wikipedia.org/wiki/Kombinatorika

class permutations:
    l = 0
    n = []
    a = []

    def __init__(self, n):
        self.n = n
        self.l = len(n)
        self.a = [None] * len(n)

    def __iter__(self):
        return self._ca(self.n)

    def __len__(self):
        return len(self.n)

    def _ca(self, n):
        for i,k in enumerate(n):
            o = self.l - len(n)
            if len(n) > 0:
                self.a[o] = k

            if o == self.l-1:
                yield self.a
                            
            p = n[:i] + n[i+1:]

            yield from self._ca(p)

