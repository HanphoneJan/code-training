import sys

while True:
    s = input().split()
    a,b = int(s[0]),int(s[1])
    if not a and not b:
        break
    print(a+b)