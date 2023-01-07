"""part1
def rpst (l):
    if l[0]=='A':
        a=1
    elif l[0]=='B':
        a=2
    else:
        a=3
    if l[2]=='X':
        x=1
    elif l[2]=='Y':
        x=2
    else:
        x=3
    return a,x

def rpsr (a,x):
    if x==a: #empate
        return 3
    dif=x-a
    if dif==1 or dif==-2:
        return 6
    return 0


res=0
with open('/home/vlam94/slither/advent/d2-i.txt') as f:
    for line in f:
        a,x = rpst(line)
        res+=rpsr(a,x)+x
    print(res) """

#part 2
def rpsc (l):
    if l[0]=='A':
        a=1
    elif l[0]=='B':
        a=2
    else:
        a=3
    if l[2]=='X':
        x=0
    elif l[2]=='Y':
        x=3
    else:
        x=6
    return a,x   

def rpsr (a,x):
    if x==3:
        return 3+a
    if x==6:
        if a==3:#ganhar de tesoura
            return 7
        return 6+a+1
    if a==1:#perder de pedra
        return 3
    return a-1


res=0
with open('/home/vlam94/slither/advent/d2-i.txt') as f:
    for line in f:
        a,x = rpsc(line)
        res+=rpsr(a,x)
    print(res) 

 
