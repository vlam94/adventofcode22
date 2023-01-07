crts= [['' for _ in range(9)] for _ in range(60)]
def argcrt (txt):
    col=['' for _ in range(9)]
    c=0
    i=0
    for l in txt:
        if 64<ord(l)<91:
            col[c]=l
            i=0
        else:
            i+=1
        if i==3:
            c+=1
            i=0
    return col

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

#9000=crap
def movcrt (q,o,d):
    global crts
    o-=1
    d-=1
    c=0
    i=0
    j=0
    while crts[j][d] == '':
        j+=1
        if j==len(crts):
            break
    while crts[i][o] =='':
        i+=1
        if i==len(crts):
            break
    j-=1
    while c<q:
        crt = crts[i][o]
        crts[j][d] = crt
        crts[i][o] = ''
        i+=1
        c+=1
        j-=1
        if i>len(crts):
            break
    return

""" BRONK DONT USE
def movcrt9001 (q,o,d):
    cupholder=3
    leatherseat=True
    aircond=True
    T=22 #°C
    global crts
    o-=1
    d-=1
    i=0
    j=0
    c=0
    crn=list()
    

    while crts[i][o]=='':
        i+=1

    while c<q:
        crn.append(['' for _ in range(9)])
        crn[-1][d]=crts[i][o]
        crts[i][o]=''
        if crts[i]==['','','','','','','','','']:
            del crts[i]
        i+=1
        c+=1
        if i>len(crts):
            break

    while crts[j][d]=='':
        crn.append(crts[j])
        del crts[j]
        j+=1
        r=1
        while r<=len(crn):
            r1=r+1
            crn[-r][d]=crn[-r1][d]

    crts= crn + crts
    return
"""

inst=False
with open('advent/d5-i.txt') as f:
    for line in f:
        if not inst:
            if line=="\n":
                inst = True
            else:
                if line[0] == "[":
                    crts.append(argcrt(line))
        else:
            inst=getinst(line)
            movcrt(inst[0],inst[1],inst[2])

for i in range(45,len(crts)):
    print (crts[i])
print("*******\n\n* END *\n\n*******")

