"""
Collatz conjecture
"""
# The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

import matplotlib.pyplot as plt

def number_of_steps_to_finish_collatz_sequence(n):
	step_index = 0
	if n <= 0 or (n%2 != 0 and n%2 != 1):
		print("Re-select a positive integer (Z+)")
	else:
		while n != 1: # the sequence does not reach 1.0
			if n%2 == 0:
				step_index += 1
				n = n/2
			elif n%2 == 1:
				step_index += 1
				n = 3*n + 1
		return(step_index)
		
test_numbers_list = []
steps_index = []

for test_numbers in range(1,100000000000000,10000000000):
	test_numbers_list.append(test_numbers)
	steps_index.append(number_of_steps_to_finish_collatz_sequence(test_numbers))

fig = plt.figure(figsize=(150,10))
plt.plot(test_numbers_list,steps_index)
plt.title("The steps (y-axis) when a Z+ (x-axis) reach 1 via Collatz function")
plt.grid(True)
plt.show()