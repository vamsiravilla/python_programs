1. Write a program to print the following Patterns
  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5

program:

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.Write a program to print the following Pattern
  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1 

program:

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1

program:

n = 5
for i in range(1,6):
    for j in range(1,n+1):
        print(n-i,end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4.Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5

program:

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5

program:

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15

program:

n = 5
num = 1
for i in range(0, n):
    for j in range(0, i+1):
        print(num, end=" ") 
        num = num + 1
    print(" ") 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1

program:

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    n-=1
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 

program:

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
        i+=1
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O

program:

n = 5
num = 65
for i in range(0, n):
    for j in range(0, i+1):
        ch = chr(num)
        print(ch, end=" ")  
        num = num + 1
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 

program:

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * 

program:

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print(" ")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

12.Write a program to print the following Pattern
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * 
program:

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n):
            print("*",end=' ')
        else:
            print(" ",end=" ")
            
    print()

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

13.Write a program to print the following Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * *

program:

n = 5
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

14.Display Multiplication Table in given range using Nested for loops

program:

n = 6
for i in range(1,n+1):
    print(i,"table")
    for j in range(1,11):
        c = i*j
        print(i,'x',j,'=',c)
    print()

output:

1 table
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 table
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

3 table
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

4 table
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 table
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 table
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

15.Display Prime Numbers in the given range using nested for loops 

program:

max = int(input('Enter the max integer: '))
for number in range(2, max+1): 
    is_prime = True
    for interval_num in range(2, number):
        if number % interval_num == 0:
            is_prime = False
            break

    if is_prime:
        print(number)

output:

Enter the max integer: 20
2
3
5
7
11
13
17
19

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

16.Write a program to print the following Pattern
	1
              3  2
       6   5   4
10  9   8   7

program:

k = 0
for i in range(1,5):
    print(" "*(4-i),end=" ")
    for j in range(k+i,k,-1):
        print(j,end=" ")
    print()
    k=k+i

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

17.Write a program to print the following Pattern
10  9  8   7
      6   5  4
           3  2
               1
 
program:

n=10
for i in range(5):
    for j in range(5):
        if j>i:
            print(n,end=' ')
            n-=1
        else:
            print(' ',end=' ')
    print()
   


  