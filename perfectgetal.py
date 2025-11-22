def deler(n):
    dlst=[]
    if n % n**(1/2)==0:
        dlst.append(int(n**(1/2)))
    for k in range(1,int(n**(1/2))+1):
        if k==1:
            dlst.append(k)
        if k>1:
            if n%k==0:
                if k!=n:
                    dlst.append(k)
                    dlst.append(n/k)
    return dlst
print(deler(6))
def perfect(r):
    delers=deler(r)
    som=0
    for f in delers:
        som+=f
    if som==r:
        return True
    else:
        return False
print(perfect(6))
wow=[]
for w in range(1,10000):
    if perfect(w):
        wow.append(w)
print(wow)