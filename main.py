#!/bin/env python
#encoding: utf-8
from collections import Counter
import re
import sys

def clear_and_convert_to_int(line):
	line = re.findall("\d+" , line)
	line = map(lambda x: int(x), line)
	return line

def f(x):
	return x % 2 != 0 and x % 3 != 0

def diff(k, seq):
	k = int(k)
	cs = Counter(seq)
	res = 0
	for key, value in cs.items():
		if key + k in cs:
			res += value * cs[key + k]
	# a = tuple(filter(f, sorted(q)))
	return res

def main():
	n,k = sys.stdin.readline().split(' ')
	el = sys.stdin.readline()

	seq = sorted(clear_and_convert_to_int(el))
	#print seq
	print diff(k, seq)

if __name__ == "__main__":
	main()

