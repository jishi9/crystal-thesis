#!/usr/bin/python
from collections import defaultdict

cells = '0& 1& 2& 3& 4& 5& 6& 7& 8& 9& 10& 11'
node_sets = '16,15,8,6  & 10,19,9,0 & 8,6,12,14 & 15,3,6,2  & 18,7,10,19 & 13,13,7,16 & 7,16,19,8  & 6,2,14,11 & 4,5,15,3  & 1,17,18,7 & 19,8,0,12  & 13,4,16,15'

cells = map(int, cells.split('&'))
node_sets = node_sets.split('&')
node_sets = [ map(int, s.split(',')) for s in node_sets ]

n2cs = defaultdict(set)
for c, ns in zip(cells, node_sets):
	for n in ns:
		n2cs[n].add(c)
n2cs = list(n2cs.iteritems())



def mkset(iterable, base):
	return '\{%s\}' % ','.join('%s_{%d}' % (base, val) for val in iterable)

print '{\\begin{tabular}{|ccc|}'
print 'cell & $\\mapsto$ & vertices \\\\'
for c, ns in zip(cells, node_sets):
	print '$c_{%d}$ & $\\mapsto$ & $%s$ \\\\' % (c, mkset(ns, 'n'))
print '\\end{tabular}}'


print '\n\n'


print '{\\begin{tabular}{|ccc|}'
print 'vertex & $\\mapsto$ & cells \\\\'
for n, cs in n2cs:
	print '$n_{%d}$ & $\\mapsto$ & $%s$ \\\\' % (n, mkset(cs, 'c'))
# print ' & '.join(str(n) for n, _ in n2cs), '\\\\'
# print ' & '.join(mkset(cs) for _, cs in n2cs)
print '\\end{tabular}}'


print '\n\n'


print '{\\begin{tabular}{|ccc|}'
print 'vertex-set & $\\mapsto$ & cell \\\\'
for c, ns in zip(cells, node_sets):
	print '$%s$ & $\\mapsto$ & $c_{%d}$ \\\\' % (mkset(ns, 'n'), c)
print '\\end{tabular}}'
