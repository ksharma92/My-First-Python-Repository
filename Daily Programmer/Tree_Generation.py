#Learnt from someone else's code
class Tree_Generator(object):
    def __init__(self, tree_format):
        temp, self.root, self.leaf = tree_format.split()
        self.base = int(temp)
        
    def build_tree(self):
        temp_dist = (self.base / 2) - 1
        for i in range(1, self.base + 1, 2):
            if temp_dist < 0:
                print self.leaf * i
            else:
                print " " * temp_dist, self.leaf * i
            temp_dist -= 1
            
        print " " * ((self.base / 2)- 1) + self.root * 3
        
tree_g = Tree_Generator(raw_input("Enter string format"))
tree_g.build_tree()
                
        
