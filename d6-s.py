def mrkcnt(txt,n):
    chk=[]
    con=0
    for l in txt:
        con+=1
        chk.append(l)
        if len(chk)<=n:
            continue
        del chk[0]
        for c in chk:
            mrk=bool(chk.count(c)==1)
            if not mrk:
                break
        if mrk:
            return con           
    return con


with open('advent/d6-i.txt') as f:
    for line in f:
        n=int(input("How many chars? "))
        c=mrkcnt(line,n)
print(c)

