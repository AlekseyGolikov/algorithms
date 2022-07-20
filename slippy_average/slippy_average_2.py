
import functools

def slippy_average_2(k, n):
	l = range(1, n + 1)
	for _ in range(k, n+1):
		buf = l[_-k:_]
		print(float(functools.reduce(lambda x,y: x+y, buf) / k))

if __name__ == '__main__':
	slippy_average_2(4,7)
