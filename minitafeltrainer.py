list=[]
for n in range(1,11):
    list.append(int(n))


for e in range(1,11):
    nlist = []
    for g in range(0,10):
        nlist.append(list[g]*int(e))
    print(nlist)