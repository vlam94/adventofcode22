
def trsl(txt):
    n=[]
    j=0
    for l in txt:
        if l.isnumeric():
            if j==0:
                n.append(int(l))
                j+=1
            else:
                n[-1]=n[-1]*10**j+int(l)
        else:
            j=0
    return n 

def camp(dat):
    if dat[0]==dat[2] or dat[1]==dat[3]:
        return [True,True]                  #       ..0___1..
    c1=bool(dat[2]>dat[0] and dat[3]>dat[0])#part 1 ...2_____
    c2=bool(dat[3]<dat[1] and dat[2]<dat[1])#       _____3...
    if not c1 and not c2 or c1*c2:         
        return [True,True]                                                        #       ..0___1..
    c3= bool(dat[2]<=dat[1] and dat[3]>dat[1] or dat[1]<=dat[2] and dat[1]>dat[3])#part 2 ...2____3
    c4= bool(dat[3]>=dat[0] and dat[2]<dat[0] or dat[0]>=dat[3] and dat[0]<dat[2])#       2____3...
    if c3 or c4:
        return [False,True]
    return [False, False]


cont=cont2=0
with open('advent/d4-i.txt') as f:
    for line in f:
        dup=trsl(line)
        cond=camp(dup)
        if cond[0]:      #part 1
            cont+=1
        if cond[1]:      #part 2
            cont2+=1
print("%i groups are contained within others\n%i groups overlap\n%i groups ok\nCaio otario" %(cont,cont2,1000-cont2))


            
        