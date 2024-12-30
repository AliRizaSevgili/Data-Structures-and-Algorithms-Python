# Analysis and Reflection for Lab 3

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):  		#1 unit time is taken to compare
		return 1		#1 unit time is taken to compare
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

The function calculates value^number recursively.

    Base Case:
        If number == 0, returns 1.
        If number == 1, returns value.
    Recursive Case:
        If number > 1, returns value * function1(value, number - 1).

Time Complexity:

    O(number): The function makes number recursive calls.

Space Complexity:

    O(number): Due to the recursive call stack.

This function works but can be inefficient for large number values.

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):				#1 unit time
		return True
	else:
		if(mystring[a] != mystring[b]):	#1 unit time
			return False		#function ends
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```
In function2, we call recursive_function2() with the string, starting index a = 0, and ending index b = length - 1. In recursive_function2(), if a >= b, the function returns, meaning it terminates. This indicates that a can increase up to half the length of the string, and b can decrease down to half the length of the string.

In the else block, if the characters at indices a and b are not the same, the function returns, meaning it ends without making further recursive calls. However, if none of these conditions are met, the function calls itself again with a incremented by 1 and b decremented by 1.

Therefore, a and b are adjusted with each recursive call, and the maximum number of iterations is half the length of the string, i.e., n/2 (where n is the string length). Each recursive call takes 2 units of time, so for n/2 iterations, the total time is:
Total Time=2×(n/2)=n
Total Time=2×(n/2)=n

Thus, the time complexity is T(n) = O(n).

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```
In each function call, the execution time is 3 units. The number of iterations (or function calls) depends on the value of n. With each recursive call, the input to the function is halved, meaning the function is called with n/2 in each step.

For the base cases, we have:

    T(0) = 0 and T(1) = 1.
    If n is even, the recurrence relation becomes T(n) = 6 + T(n/2).
    If n is odd, the recurrence is T(n) = 7 + T(n/2).

The recursive relation can be expanded as follows:

    T(n) = 7 + T(n/2),
    T(n/2) = 7 + T(n/4),
    So, T(n) = 7 + 7 + T(n/4), which expands further as:
    T(n) = 7 * 2 + T(n/2^2),
    T(n) = 7 * 3 + T(n/2^3),
    In general, T(n) = 7 * k + T(n/2^k), where the final call results in T(1).

The total number of function calls corresponds to halving n repeatedly until we reach 1. Thus, after k calls, we have n/2^k = 1. Solving this gives:
n≥2k−1
n≥2k−1

Taking the logarithm of both sides:
log⁡2(n)≥k−1
log2​(n)≥k−1

Thus, k = \log_2(n) + 1, where k is the total number of function calls.

Since each call takes 3 units of time, the total time is:
Total Time=3×k=3×(log⁡2(n)+1)=3log⁡2(n)+3
Total Time=3×k=3×(log2​(n)+1)=3log2​(n)+3

Therefore, the time complexity is O(log_2(n)).

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
To write a recursive function, you first define the function (like factorial) and give it the necessary inputs. Every recursive function needs at least one base case—this is the simple situation where the problem can't be broken down any further, and the answer is easy to calculate. The base case handles this simple case, while the recursive part of the function breaks the problem down and calls itself to work on smaller parts of the problem.

For example, in Lab 3 (in function 1), the factorial function shows two key elements of recursion:

    Termination condition: This is when the function stops calling itself. In the factorial example, the condition is n == 0.
    Reduction step: This is where the function calls itself with a smaller version of the problem. For factorial, it's factorial(n-1).

When you call the function with a positive number, it keeps calling itself with smaller numbers, multiplying each one by the result of the next, until it reaches 1 or 0. This is the base case, which ends the recursion. Without a base case, the function would keep running forever.
Example:



def factorial(n):
    # Base case: when n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by the result of factorial(n-1)
    return n * factorial(n - 1)

In this function, factorial(5) breaks down into 5 * factorial(4), and so on, until it hits factorial(0) or factorial(1), which ends the recursion.


2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
When analyzing recursive functions compared to non-recursive ones, you start by declaring the necessary variables and functions for both types. Then, you go through each line of code, counting what happens and how it impacts the final result. This can be done by adding comments next to each line or writing out what the line does. For example, you can note how many times a loop runs or how often a condition is checked.

After this, you create the mathematical expression for T(n) by summing up the operation counts from the comments. This step is unique to recursive functions since it helps simplify the equation, something that’s not typically needed for non-recursive functions.

Finally, you simplify the expression, state your result, and conclude with the time complexity, such as T(n) or O(n).
