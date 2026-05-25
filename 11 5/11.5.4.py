n = int(input())
odwrocona_d = 0
i = 10
while n>0:
    pom = n%10
    zamiana = 9-pom
    odwrocona_d = odwrocona_d*i + zamiana
    n = n//10
d = 0
while odwrocona_d>0:
    pom = odwrocona_d%10
    d = d*10 + pom
    odwrocona_d = odwrocona_d//10
print(d)
