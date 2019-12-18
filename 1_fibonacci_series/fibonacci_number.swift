// import Foundation
// import Cocoa

import Python
// %include "EnableIPythonDisplay.swift"
// IPythonDisplay.shell.enable_matplotlib("inline")
let plt = Python.import("matplotlib.pyplot")

let index = 90

if index >= 3 {
	var index_list = [1, 2]
	var fibo_list = [1, 1]
	var fibo1 = 1
	var fibo2 = 1
	var i = 3
	var fib_next = 0
	
	while i <= index {
		fib_next = fibo1 + fibo2
		index_list.append(i)
		fibo_list.append(fib_next)
		i += 1
		fibo1 = fibo2
		fibo2 = fib_next
	}
	// print(fibo_list)
	plt.plot(index_list, fibo_list)
	plt.show()
	
} else {
	print("at least first three of fibonacci number")
}

