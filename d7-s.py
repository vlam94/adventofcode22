ls = bool()
cd = bool()
mem = list()
now = []
lvl = 0

def getcom(txt):
    global ls,lvl,now
    if txt[3] == 'l':
        return True

    if len(mem)>0:
        if txt[5]=='.':
            lvl-=1
            del now[-1]
            return False
        srch=[]
        for i in range(5,len(txt)):
            srch.append(txt[i])





def getinst (txt):
    for i, j in enumerate(mem):
        found=bool(j==dir)
        if j == dir:
            pos=i

    

with open('advent/d6-i.txt') as f:
    for line in f:
        if line [0]=="$":
            ls = getcom(line)
