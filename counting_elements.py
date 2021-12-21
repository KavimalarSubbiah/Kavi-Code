a=eval(input())
k={}
for i in range(len(a)):
   p=a.count(a[i])
   k[a[i]]=p
print(k)