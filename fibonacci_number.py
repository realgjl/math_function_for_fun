import matplotlib.pyplot as plt

def fibonacci(index):
	if index >= 3:
		index_list = [1,2]
		fibo_list = [1,1]
		fibo1 = 1
		fibo2 = 1
		i = 3
		while i <= index:
			fib_next = fibo1 + fibo2
			index_list.append(i)
			fibo_list.append(fib_next)
			i += 1
			fibo1 = fibo2
			fibo2 = fib_next
		# return(index_list, fibo_list)
		fig = plt.figure(figsize=(15,7))
		plt.plot(index_list, fibo_list)
	else:
		print("at least first three of fibonacci number")
		
fibonacci(3)
# fibonacci(10)
# fibonacci(20)
# fibonacci(50)
# fibonacci(70)
# fibonacci(100)
# fibonacci(150)
# fibonacci(200)
# fibonacci(500)
# fibonacci(1000)
# fibonacci(1300)