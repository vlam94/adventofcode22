elfm = [0,0,0]
c1=0
with open('/home/vlam94/slither/advent/d1-i.txt') as f:
    for line in f:
        if line=='\n':
            c2=c1
            c1=0
            if c2>elfm[0]:
                elfm[0]=c2
                elfm.sort()
        else:
            c1+=int(line)      
print(sum(elfm))
