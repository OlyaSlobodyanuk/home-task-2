import random
import sys

n = int(sys.argv[1])
count = 0
for i in range(0, n):
	for f in range(0, 2):
		r = random.randint(1, 6)
		#print("%i тест = %i" % (i, r))
		if(r == 6):
			count += 1
			break
prob = count / n
print("Вероятность = %.3f" % prob)