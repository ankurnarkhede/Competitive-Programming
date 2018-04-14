
# 6
# 3 6 1 1
# .@@..@
# .....@
# @.@.@@


import sys

import numpy as np

n = int(input()) # NO. of testcases

def is_possible(a, i, j):
	'''
	a is ndarray and i and j are coordinates to check
	'''
	p,q,r,s = a[:i,:j], a[:i, j:], a[i:, :j], a[i:, j:]

	n = np.count_nonzero(p)
	print(n)
	if np.count_nonzero(q) == n and np.count_nonzero(r) == n and np.count_nonzero(s) == n:
		return True
	else:
		return False

for _ in range(n):
	r,c,h,v = [ int(i) for i in input().strip().split() ]
	waffle_array = []
	for line in range(r):
		t = [] # One row of the array
		for character in input().strip():
			if character == '.':
				t.append(0)
			if character == '@':
				t.append(1)
		waffle_array.append(t)

	waffle_array = np.array(waffle_array)
	if np.count_nonzero(waffle_array) == 0:
		print("Case #{}: POSSIBLE".format(_+1))
	else:
		flag = False
		for i in range(1, r+1):
			for j in range(1, c+1):
				if is_possible(waffle_array, i, j):
					print("Case #{}: POSSIBLE".format(_+1))
					flag = True
					break

		if not flag:
			print("Case #{}: IMPOSSIBLE".format(_+1))