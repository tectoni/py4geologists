#!/usr/bin/python

counts = dict()
names = ['john', 'terry', 'elisa', 'peter', 'elisa', 'romain']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

