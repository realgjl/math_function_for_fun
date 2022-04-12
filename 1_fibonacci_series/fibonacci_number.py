import matplotlib.pyplot as plt

def fibonacci(Nth_fibonacci_number):
    x_axis = [i for i in range(1,Nth_fibonacci_number+1)]
    fibonacci_list = [1,1]
    for i in range(2, Nth_fibonacci_number): # min of N is 3 <=> min of index is 2
        new_fibonacci_number = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(new_fibonacci_number)
    return(fibonacci_list, x_axis)


return_list, x_axis = fibonacci(8) # Nth_fibonacci_number>=2
print(return_list)
