class Node:

    def __init__(self, data):

        self.left = None

        self.right = None
        self.order=0
        if (data):
            self.order=1

        self.data = data
    def insert(self, data):
        if self.data:
            if (data < self.data):
                if  self.left:
                    self.left.insert(data)

                else:
                    self.left=Node(data)


            else:
                if self.right:
                    self.right.insert(data)

                else:
                    self.right=Node(data)


            return 1

        self.data = data

        return 1

    def PrintTree(self):
        print( self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

    def exits(self,value):
        if self.data == value:
            return True
        if  value > self.data:
            if self.right:
                return self.right.exits(value)
        if self.left:
            return self.left.exits(value)
        return  False

    def get_levels(self):
        return  self.aux_get_levels(0,{0:[]})
    def aux_get_levels(self,levels,result):
        if not levels in result:
            result.update({levels:[]})

        result[levels]=result[levels]+[self.data]
        levels=levels+1
        if self.left:
            result=self.left.aux_get_levels(levels,result)
        if self.right:
            result=self.right.aux_get_levels(levels,result)
        return result

    def avg_by_level(self):
        return  map (  lambda  x: sum(x)/len(x) ,self.avg_by_level().values())

    def get_level_by_value(self,value,level):

        if self.data==value:
            return level
        if value < self.data:
            if self.left:
                return  self.left.get_level_by_value(value,level+1)
        else :
            if self.right:
                return  self.right.get_level_by_value(value,level+1)
        return -1








    # root = Node(12)
#
# root.insert(6)
# root.insert(14)
# root.insert(3)
#root.PrintTree()
#print ( root.exits(114) )
#print ( root.get_levels() )
root = Node(4)
root.insert(2)
root.insert(9)

root.insert(3)
root.insert(5)
root.insert(7)


print ( ">>>>>>>>", root.get_level_by_value(5,0))
#print ( root.get_levels() )
