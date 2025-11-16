def fact(n):
    if type(n)==int and n > 0:
        a=n
        while n>1:
            a=a*(n-1)
            n=n-1
    return a
def euler(l):
    teller=0
    som=1
    j=1
    while teller <= l:
        som=som+1/(fact(j))
        j+=1
        teller+=1
    return som
print(euler(10))
#13 minuten