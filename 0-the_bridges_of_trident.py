#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import Counter
import random
import Orange

data = Orange.data.Table("bridges.tab")

print "Liczba instancji:", len(data)

print "\nPierwsze 10 instancji:"
for d in data[:10]:
    print d

# zakładamy że zmienna celu to ostatni atrubyt - TYPE
class_var = data.domain.features[-1]

print "\nNazwa zmiennej celu:", class_var.name
print "Wartości zmiennej celu:", class_var.values

print "\nHistogram zmiennej celu:"
print "%-11s %s" % ("Wartość", "L. wystąpien")
for x in class_var.values:
    print "%-11s %d" % (x, len([d for d in data if d[class_var] == x]))

cont = []
disc = []
for a in data.domain.features:
    if a.varType == Orange.feature.Type.Discrete:
        disc.append(a.name)
    else:
        cont.append(a.name)

print
print "Liczba atrybutów:", len(data.domain.features)
print "Atrybuty ciągłe:", len(cont), ':', cont
print "Atrybuty dyskretne:", len(disc), ':', disc

def average(tab):
    return sum(tab) / len(tab)

def mode(tab):
    c = Counter(tab)
    return c.most_common(1)[0][0]

print
print "%-15s %s" % ("Atrybut", "Wartość średnia/modalna")
for x in data.domain.features:    
    if x.varType != Orange.feature.Type.Discrete:
        value = average([d[x] for d in data if not d[x].is_special()])
        print "%-15s %.2f" % (x.name, value)
    else:
        value = mode([d[x].value for d in data])
        print "%-15s %s" % (x.name, value)    

print
print "Brakujące wartości:"
print "%-12s %s" % ("Atrubyt", "L. brakujących wart.")
for x in data.domain.features:
    n_miss = sum(1 for d in data if d[x].is_special())
    print "%-12s %d" % (x.name, n_miss)

print
print "Przykładowa próbka (ok. 5% instancji):"
count = int(round(0.05 * len(data)));
smpl = random.sample(range(0, len(data)), count)
for i in smpl:
    print data[i]