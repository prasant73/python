

from inputs import list_input
from math import floor, sqrt, ceil
# import math

def isPrime(n):
	for i in range(2, floor(n/2) + 1):
		if n % i == 0:
			return False
	else:return True
# print(isPrime(67))

def prime_factors(num):
	factors = [1]
	if isPrime(num):
		factors.append(num)
		return factors
	else:
		for i in range(2, ceil(num/2) + 1):
			if (num % i == 0) and (isPrime(i)):
				factors.append(i)
	return factors


def main():
	dict_of_factors = []
	l1 = list_input(int(input("enter the number of numbers you want to find the prime factors of : ")))
	# l1 = [1,2,3,4]

	for i in l1:
		dict_of_factors[i] = prime_factors(i)
	print(dict_of_factors)

print("Inside prime factors", __name__)

if __name__ == "__main__":
	try:
		main()
	except MemoryError as m:
		print("memory Error", m)
	except OSError as os:
		print("oserror", os)
	except Exception as e:
		print("Inside main's Exception")
		print(e)
	finally:
		print("Inside prime factors finally", __name__)
