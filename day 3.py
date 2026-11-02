# problem link : https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

a =int(input("enter first number : "))
b =int(input("enter second number : "))
c =int(input("enter third number : "))

# ----------using function-------
# print(pow(a,b))
# print(pow(a,b,c))


# ---using operator--------
print(a**b)
print((a**b)%c)
