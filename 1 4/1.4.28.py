def powtorz_znak(n,znak):
    if n == 0:
        return ""
    return powtorz_znak(n-1,znak) + znak

n=0
while n <= 0:
    n = int(input())
znak = input()
print(powtorz_znak(n,znak))