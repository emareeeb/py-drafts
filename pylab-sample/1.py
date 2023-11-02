'''Write a program to read a string o f 4 characters from the user.Convert every character in the string to its next alphabet.
ord()-gives the unicode value of given digit
chr()-returns to the character'''

a=input("Please enter a string")
b=len(a)
i=0
while(i<=b-1):
   x=ord(a[i])
   print(chr(x+1))
   i=i+1


