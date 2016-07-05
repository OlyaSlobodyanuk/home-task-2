import random
import sys
n = int(sys.argv[1])
sum = 0
for i in range(0, n):
	r = random.uniform(-1, 1)
	print("%.4f" % r)
	sum += r
	
print("Среднее значение = %.4f" % (sum / n))