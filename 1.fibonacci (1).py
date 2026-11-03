n=int(input("Enter n: "))
a,b,steps=0,1,0

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    steps+=1

print("\nStep count:",steps)