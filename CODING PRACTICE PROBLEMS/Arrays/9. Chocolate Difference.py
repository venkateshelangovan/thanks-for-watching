"""
Given an array A of positive integers of size N, where each value represents number of chocolates in a packet.
Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate 
packets such that :

1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates
and student having packet with minimum chocolates is minimum.

Input:

The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. 
Each test case consists of three lines. The first line of each test case contains an integer N denoting the 
number of packets. Then next line contains N space separated values of the array A denoting the values of each
packet. The third line of each test case contains an integer m denoting the no of students.

Output:

For each test case in a new line print the minimum difference.

Constraints:

1 <= T <= 100
1 <=N<= 107
1 <= Ai <= 1018
1 <= M <= N

Example:

Input:
2
8
3 4 1 9 56 7 9 12
5
7
7 3 2 4 9 12 56
3

Output:
6
2

Explanation:
Testcase 1: The minimum difference between maximum chocolates and minimum chocolates is 9-3=6

"""

def ChocolateDifference(n,m,arr):
   """
   This function returns the minimum difference between maximum chocolate and minimum chocolate that is being 
   received by m students
   Input : n - number of elements in the arr
           m- number of students 
           arr- containing n chocolate packet quantity 
   returns : chocolate_diff - minimum difference between maximum chocolate and minimum chocolate that is being 
   received by m students
   
   Time Complexity : O(nlogn) # for sorting 
   """
   chocolate_diff=pow(2,64)-1
   arr=sorted(arr)
   for i in range(len(arr)-m+1):
       current_diff=arr[i+m-1]-arr[i]
       chocolate_diff=min(chocolate_diff,current_diff)
   return chocolate_diff
           
                   
# enter the number of test cases
t=int(input())
while t>0:
   n=int(input()) # enter the size of the array
   input_arr=list(map(int, input().split(' ')[:n])) # get array elements for chocolate packet size 
   m=int(input())# enter the number of students 
   print(ChocolateDifference(n,m,input_arr))
   t-=1