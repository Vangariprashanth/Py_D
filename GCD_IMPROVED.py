m=int(input("Enter the first num"))
n=int(input("Enter the second num"))
def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i)
    return(cf[-1])
print(gcd(m,n))