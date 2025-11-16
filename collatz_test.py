#Vermoeden van Collatz
def collatz(n):
    n=int(n)
    p=0
    while n > 1:
        if n % 2 ==0:
            n=n/2
            p+=1
        else:
            n=(3*n)+1
            p+=1
    if n<1:
        return 'Getal is kleiner dan 1, het vermoeden v. Collatz telt niet mee.'
    else:
        return f'Zijn vermoeden klopt!!! Oh my Collatz!!! er waren {p} bewerkingen in totaal'


print(collatz(16))
print(collatz(45))
print(collatz(0.2345))

def factori(n):
    if n>0 and type(n)==int:
        a=n
        while n > 1:
            a=a*(n-1)
            n=n-1
    return a
(factori(3))
def euler(n):
    som=1
    i=1
    p=1
    while p <= n:
        som = som+(1/factori(i))
        i+=1
        p+=1
    return som
print(euler(999))
