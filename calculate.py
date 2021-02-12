# For MATH61 HW #, Problem 9.7
import math

def factorial (n):
	if n == 1:
		return 1
	if n == 0:
		return 1

	return n * factorial(n-1)

def stirling (n):
	return math.sqrt(2*math.pi*n)*math.pow(n,n)*math.exp(-n) 

if __name__ == '__main__':
	n = int(input('Enter a number: '))

	print(f'{n}! = {factorial(n)}')
	print('Approximation: %.3f' % stirling(n))