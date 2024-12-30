# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Ali Riza Sevgili
# Student Number:135200228
#



def wins_rock_scissors_paper(player1, player2):
    player1 = player1.upper()
    player2 = player2.upper()
    if player1=='ROCK' and player2=='SCISSORS':
        return True
    elif player1=='PAPER' and player2=='ROCK':
        return True
    elif player1=='SCISSORS' and player2=='PAPER':
        return True
    else:
        return False
    

def factorial(num):
  fact = 1
  for i in range(1,num+1):
     fact*=(i)	
  return fact


def fibonacci(num):
	fib=0
	list_fib=[0,1,1]
	if num==1 or num==1 or num==2:
		fib=1
	else:
		for i in range(3,num+1):
			list_fib.append(list_fib[i-2]+list_fib[i-1])
			fib=list_fib[i]	
	return fib


def sum_to_goal(numbers, goal):
    for first_num in numbers:
        second_num = goal - first_num
        if second_num in numbers:
            return first_num * second_num
    return 0
    

class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.counter = 0

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.step_size


class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.step_size










    






