from itertools import permutations

translate = { 'a': 0, 'b': 1, 'c': 2, 'd': 3}

def order(vals):
	a, b, c, d = ( translate[v] for v in vals)
	nxt = (a + 1) % 4
	prv = (a + 4 - 1) % 4
	opp = (a + 2) % 4

	flip, flop = (1,0) if a in (0,2) else (0,1)

	if   b == nxt and d == prv: score = 4 + flip
	elif b == prv and d == nxt: score = 4 + flop
	elif b == nxt and d == opp: score = 2 + flip
	elif b == prv and d == opp: score = 2 + flop
	elif b == opp and d == nxt: score = 0 + flip
	elif b == opp and d == prv: score = 0 + flop
	else: raise Exception(a,b,c,d, nxt, prv, opp)

	# if a % 2 == 0:

	return (a, score)

for t in sorted(permutations(['a','b','c','d']), key=order):
	print '%s/%s/%s/%s,' % t,