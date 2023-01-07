"""part 1
def orgsak(s):
    tam=len(line)-1
    div=int(tam/2)
    c1=line[:div]
    c2=line[div:tam]
    org=list(set(c1)&set(c2)) #copiei isso das internet 
    org.sort()
    return org[-1]
"""

def priotot(p):
    n=0
    for l in p:
        m=ord(l)
        if m>91:
            n+=m-96
        else:
            n+=m-64+26
    return n
"""
def priotot(p):
    alf=['ç','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=0
    for l in p:
        i=0
        while l!=alf[i]:
            i+=1
        n+=i
    return n  
"""
"""
prio=[]
with open('advent/d3-i.txt') as f:
    for line in f:
        prio.append(orgsak(line)) 
print(priotot(prio))
"""
#part 2
def grplbl(g):
    org=list(set(g[0])&set(g[1])&set(g[2])) #adaptei sem entender hu3 
    org.sort
    return org[-1]

grp=[]
prio=[]
i=0
with open('advent/d3-i.txt') as f:
    for line in f:
        trm=len(line)-1
        grp.append(line[:trm])
        i+=1
        if i==3:
            lbl=grplbl(grp)
            prio.append(lbl)
            grp=[]
            i=0
    
print(priotot(prio))