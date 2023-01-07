crts=list()
for _ in range (9):
    crts.append([])

def argcrt (txt):
    global crts
    c=0
    i=0
    for l in txt:

        if 64<ord(l)<91:
            crts[i].insert(0,l)
            c=0
        else:
            c+=1
        if c==3:
            i+=1
            c=0
    return

def getinst(txt):
    inst=[0]*3
    i=0
    j=False
    for l in txt:
        if l.isnumeric():
            if not j:
                inst[i]=int(l)
                j=True
                continue
            else:
                inst[i]=inst[i]*10+int(l)
                j=False
                i+=1
        if j:
            j=False
            i+=1
    return inst

def movcrt9001 (q,o,d): #"new, much better!"
    cupholder=3
    leatherseat=True
    aircond=True
    T=22 #°C
    global crts
    o-=1
    d-=1
    crn=list()
    for _ in range(q):
        if len(crts[o])==0:
            break
        crn.append(crts[o][-1])
        del crts[o][-1]
    for c in reversed(crn):
        crts[d].append(c)
    return

def movcrt (q,o,d): #"old, YUCK!"
    o-=1
    d-=1
    for _ in range(q):
        if len(crts[o])==0:
            break
        crts[d].append(crts[o][-1])
        del crts[o][-1]
    return


inst=False
with open('advent/d5-i.txt') as f:
    for line in f:
        if not inst:
            if line=="\n":
                inst = True
            else:
                if line[0] == "[":
                    argcrt(line)
        else:
            inst=getinst(line)
            movcrt(inst[0],inst[1],inst[2])
for c in crts:
    print(c)

print("*******\n\n* END *\n\n*******")
