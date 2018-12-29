m=int(input("Enter first num"))
n=int(input("Enter second num"))

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)
    fn=[]
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)
    fc=[]
    for f in fm:
        if f in fn:
            fc.append(f)
    return(fc[-1])
print(gcd(m,n))
