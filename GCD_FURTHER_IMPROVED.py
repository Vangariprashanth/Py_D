m=int(input("Enter the first num"))
n=int(input("Enter the second num"))
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mrfc=i  #mrfc=most recent factor
    return mrfc
print(gcd(m,n))
