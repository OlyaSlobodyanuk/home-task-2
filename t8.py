import random
import sys

n = int(sys.argv[1])
count = 0
for i in range(0, n):
	sum = 0
	for f in range(0, 4):
		r = random.randint(1, 6)
		sum += r		
	
	if(sum < 9):
		count += 1		

prob = count / n
print("Вероятность = %.3f" % prob)
