n = int(input())
s=0
while n != 0:
   s = s + n%10
   n = n//10
print(s)

"""
wczytaj n
s<-0
dopóki n != 0
    s<-s+(n mod 10)
    n<-(n div 10)
wypisz s
"""