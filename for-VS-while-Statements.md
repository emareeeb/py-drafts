Python has a statement that works exclusively on collections. It examines each
element and performs any action set by the programmer until there are no more
elements left in the collection.

```python
#for statement is a looping structure.
```

We use for statement when the number of times we execute the body or the suite is
determinable(known).

We use a while statement when the number of iterations is not known in the
beginning, and we use a for statement when the number of iterations is known.

```python
**#syntax:**
for <target_variable> in <iterable> :
<suite/body of for>
```

iterable:

- an Iterable is a collection of elements physically or conceptually .
- it has a built-in mechanism to give an element each time we ask.
- has a built-in mechanism to signal when there are no more elements.

>> Semantics of the for statement:

1. start iterating through the iterable.
2. get one element to the target variable.
3. execute the suite or the body.
4. repeat steps 2 and 3 until the iterable signals that it has no more elements.
5. Exit the for loop and move to the next statement.

>> Examples:

Given a list of numbers, the list contains 4 elements namely, 1 2 3 and 4. The variable
value gets the element 10 the 1st time and that is displayed as part of the loop body,
value gets the element 20 the 2nd time and displays it and so on until there are no
more elements to be copied to value . the iteration stops when there are no more
elements in the list.
#using list

```python

num = [10,20,30,40]
for value in num:
print(value)

'''OUTPUT- 
10
20
30
40'''
```

#using strings

<aside>
💡 #Program to find sum of numbers from 1 to entered number.

</aside>

```python
n=int(input("Please enter the number till where you would like to obtain the sum of all numbers")
sum=0
for i in range(1,n+1):
	sum=sum+i
print(sum)
```

<aside>
💡 #Program to display square of all numbers till an entered number.

</aside>

```python
n=int(input("Enter the number till where you would like to see the square of all numbers"))
i=1
while i<=n:
	print("Square of",i,"is",i*i)
	i=i+1

#Same program using "for loop":
n=int(input("Enter the number till where you would like to see the square of all numbers"))
for i in range(1,n+1):
	print("Square of",i,"is",i*i)
	i=i+1

'''Output for both the programs are the same, but in this scenario, since the number
of iterations are known at the beginning itself, it is better to use for since we do not
need to take into consideration the initialization of the loop variable and updation
and is done implicitly. Thus in this scenario, use of for is better than use of while.'''
```

<aside>
💡 #Write a program to display all squares less than or equal to n

</aside>

```python
#Since we cannot easily determine the number of iterations. We should use a while
#loop here.
#using while
n = int(input("enter an integer : "))
i = 1
while i * i <= n :
	print("Square of ", i, " is ", i * i)
	i += 1 #(i=i+1)

#using for
n = int(input("enter an integer : "))
for i in range(n):
	if (i*i) < n:
		print("Square of ", i, " is ", i * i)

'''This results in the same outcome, but the number of times the loop runs is always
going to be n. whereas when we use while it stop as soon as the square reaches
the value of n.'''
```

<aside>
💡 Program to display the factors of entered number.

</aside>

```python
n=int(input("Enter the number whose factors you'd like to obtain")
for i in range(1,n+1):
	if n % i == 0:
		print(i)
		i=i+1

#using while: (A better approach)
n = int(input("enter a number : "))
i = 1
while i * i < n :
	if n % i == 0 :
		print(i, n // i, end = " ")
			i += 1
if i * i == n :
	print(i, end = " ")
```
