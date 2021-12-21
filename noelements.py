a=eval(input())
l=len(a)
for i in range(0,l):
    count=1
    for j in range(i,l):
        if a[i]==a[j]:
            count=count+1
print(count)