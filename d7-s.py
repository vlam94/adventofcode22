class Node:
    def __init__ (self,name, isdir, parent,  size =0):
        self.name = name
        self.isdir = isdir
        self.parent = parent
        self.size = size
        self.children = isdir
        if self.children:
            self.children = list()
    
    def __str__(self,level=0):
        ret=str()
        fileordir = ["file","dir"]
        ret += f'{" |" * level} - {self.name}({fileordir[int(self.isdir)]}): {self.size}\n'
        if self.children: 
            for child in self.children:
                ret+=child.__str__(level+1)
        return ret

    def makeNode(self,line,container):
        if line.startswith("$ ls") or line.startswith("dir"):
            return False
        if line.startswith("$ cd"):
            new_dir = line.replace("$ cd ","")
            return Node(new_dir,True,container)
        new_file = line.split(' ')
        return Node(new_file[1],False,container,int(new_file[0]))

    def treeGen(self,textfile):
        
        with open (textfile) as f:
            f_lines=f.readlines()[1:]
            dir= self
            for line in f_lines:
                if line.startswith("$ cd .."):
                    dir = dir.parent
                    continue
                next_node=self.makeNode(line.strip(),dir)
                if not next_node:
                    continue
                dir.children.append(next_node)
                if next_node.isdir:
                    dir=next_node
        return
    
    def sumDirsSize(self):
        if not self.children:
            return self.size
        sum=0
        for child in self.children:
            if child.isdir:
                sum+=child.sumDirsSize()
            sum+=child.size
        self.size=sum
        return sum
    
    def findSmallDirs(self,small_size,small_dirs):
        if self.size ==0:
            self.sumDirsSize()
        if self.isdir:
            for child in self.children:
                child.findSmallDirs(small_size,small_dirs)
            if self.size < small_size and self not in small_dirs:
                small_dirs.append(self)
        return small_dirs

    def sumSmallDirs(self,small_size):
        sum=0
        for dir in self.findSmallDirs(small_size,list()):
            print(f'{dir.name} - {dir.size}')
            sum+=dir.size
        return sum
                


root = Node('\\',True, None)
root.treeGen("adventofcode22/d7-i.txt")
print(f'{root.sumSmallDirs(100000)}')



            



