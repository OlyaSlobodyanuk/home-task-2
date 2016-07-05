import math
import sys

def ln(n):
	return math.log(n)

def IsPositive(n):
	if n > 0 : 
		return True
	else:
		return False

def ShowPositiveResult(n, m):
	print("ln(%s) = %.6f" % (n, m))

def ShowNegativeResult(n):
	print("ln(%s) is illegal" % n)

def CalculateLn(n):
	arg = float(n)
	if IsPositive(arg):
		ShowPositiveResult(arg, ln(arg))
	else:
		ShowNegativeResult(arg)

def FirstCycle():
	for r in sys.argv[1:]:
		CalculateLn(r)

FirstCycle()