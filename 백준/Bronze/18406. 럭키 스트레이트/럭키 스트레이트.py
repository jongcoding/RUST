n=input()
front=n[:len(n)//2]
back=n[len(n)//2:]
a=0
b=0
for i in front:
    a+=int(i)
for j in back:
    b+=int(j)
if a==b:
    print("LUCKY")
else:
    print("READY")