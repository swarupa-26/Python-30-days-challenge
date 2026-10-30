# Task (https://www.hackerrank.com/challenges/symmetric-difference/problem)

# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# SET 1
n = int(input())
s1=set(map(int, input().split()))

# SET 2
m = int(input())
s2=set(map(int, input().split()))

a=(s1 ^ s2)
a=list(a)
for i in a:
    print(i)




