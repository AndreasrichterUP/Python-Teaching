

class Point:
    def __init__(self, No,Xw,Yw,Zw,xI,yI):
        self.No,self.Xw,self.Yw, self.Zw, self.xI, self.yI = No,Xw,Yw,Zw,xI, yI

        
    def add(self, other):
        return Point(self.No,self.Xw + other.Xw,self.Yw + other.Yw,self.Zw + other.Zw,self.xI + other.xI, self.yI + other.yI)

    def subtr(self, other):
        return Point(self.No,self.Xw - other.Xw,self.Yw - other.Yw,self.Zw - other.Zw,self.xI, self.yI)
    
    def println(self):
        print("( {}, {},{}, {}, {}, {})".format(self.No ,self.Xw, self.Yw, self.Zw, self.xI, self.yI))

if __name__ == '__main__':
    p1 = Point(5, 1361.29,  -1402.17,  200,   0.110,   0.110,)
    p2 = Point(6, 1337.27,  -1019.37,  210,   0.080,   0.110,)
    p1.println()
    p2.println()
    p1.add(p2).println()
    #sys.exit(0)
###