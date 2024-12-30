# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0; 			 # 1

	for i in range(0,number):	# n +1 
		x = (i+1)  		# n * 2
		total+=(x*x)		# n * 2

	return total			# 1
					# T(n) = 1 + n + 1 + 2n + 2n +1 = 5n + 3
					# T(n) = O(n)
```

### function 2:

Analyze the following function with respect to number 

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6    # 6
                                                          #  # T(n) = O(1) = 6


```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):			# 1 + (n - 1)

		for j in range(0,len(list)-1-i):       # n (1 + (n - 1) + 2) = (n(n + 1)) / 2 = 0.5n2 + 2.5n - 3

			if(list[j]>list[j+1]):	       # 7 * 0.5n2 - 0.5n = 3.5n2 - 3.5n

				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp
							# T(n) = O(n^2)


```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1					 # 1

	for i in range(1 to number):		# (n - 1) + 1

		total=total*(i+1)		# 1 + 1

	return total
```

					# T(n) = O(n)


## In class portion


### Group members
List the members of your group member below:

	* Sithila Jithnuka Batagoda
	* Ali Riza Sevgili
	* Veysel Topral
 	* Canberk Secilmez

### Timing Data
![image](https://github.com/user-attachments/assets/6edcde46-2195-4af6-bef3-1fe4f5180a90)

![image](https://github.com/user-attachments/assets/79e86b93-946b-41f1-a591-acae27b31ae2)


![image](https://github.com/user-attachments/assets/8fb44666-7f18-400e-a3ab-8a6bf931d4e3)

![Screenshot 2024-09-21 233428](https://github.com/user-attachments/assets/38c572b5-2b2d-47c7-89cc-8f85da6963fc)





### Summary 
|function| runtime based on analysis | Most similar curve | 
|---|---|---|

|partb_one()|  0.02864772700195317|  1000| 
	       0.129361205999885     2000 

|partb_two()|  0.00023972700000740588 |1000|
		0.0004335879966674838  2000

|partb_three()| 0.00014830699728918262  |1000|
		0.0003507839974190574   2000

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.


## Reflection:



1. For each function, what growth rate best matches your results?

    Function 1: Linear, O(n). Matches a linear curve.
    Function 2: Constant, O(1). Matches a constant curve.
    Function 3: Quadratic, O(n²). Matches a quadratic curve.
    Function 4: Linear, O(n). Matches a linear curve.

2. Does your analysis match your results? If not, where do you suppose the error occurred?

    Yes, the analysis matches the results for all functions.
    If errors occurred, they might be due to small input sizes or implementation inefficiencies, but none were observed.

3. What conclusions can you draw based on your observations?

    Direct computation (as in function2) is much faster than iteration.
    Algorithm efficiency is key: functions with O(n) are manageable for large inputs, while O(n²) functions (like function3) become inefficient.
    Choosing the right approach can drastically improve performance.
