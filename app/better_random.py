import random as rand

random = rand.random
randint = rand.randint

def choice(lis):
	"""choice funcion with weight."""
	final_lis = []
	for i in lis:
		final_lis += i[1] * [i[0]]
	return rand.choice(final_lis)
