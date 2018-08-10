n=int(input())
a=[int(i)for i in input().split()]
b=[int(i)for i in input().split()]

c=[i+j for i,j in zip(a,b)]
for i in c:
    print(i ,end=" ")
