

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



def calcDifferentials(PointMatIn):
    import numpy as np
    import RotationMatrixTools as rotMat

    print('Input Array has Dims: {} '.format(PointMatIn.shape))
    print('calc deltas of Points')
    PointMatIn[1,1:4]=PointMatIn[1,1:4]-PointMatIn[5,1:4]
    PointMatIn[2,1:4]=PointMatIn[2,1:4]-PointMatIn[5,1:4]
    PointMatIn[3,1:4]=PointMatIn[3,1:4]-PointMatIn[5,1:4]
    PointMatIn[4,1:4]=PointMatIn[4,1:4]-PointMatIn[5,1:4]


    print('===========================')
    print(PointMatIn)

    print('calc UVW')
    
       
    R=rotMat.RyprG(PointMatIn[5,6],PointMatIn[5,5],PointMatIn[5,4]).T

    #U....index:6
    #V....index:7
    #W....index:8

    PointMatIn[1,6:9]=np.dot(R,PointMatIn[1,1:4])
    PointMatIn[2,6:9]=np.dot(R,PointMatIn[2,1:4])
    PointMatIn[3,6:9]=np.dot(R,PointMatIn[3,1:4])
    PointMatIn[4,6:9]=np.dot(R,PointMatIn[4,1:4])

    print('===========================')
    print(PointMatIn)

    print('calc lger')

    PointMatIn[1,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[1,6]/PointMatIn[1,8], PointMatIn[0,2] -       PointMatIn[0,0]*PointMatIn[1,7]/PointMatIn[1,8] ]

    PointMatIn[2,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[2,6]/PointMatIn[2,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[2,7]/PointMatIn[2,8] ]

    PointMatIn[3,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[3,6]/PointMatIn[3,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[3,7]/PointMatIn[3,8] ]

    PointMatIn[4,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[4,6]/PointMatIn[4,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[4,7]/PointMatIn[4,8] ]

   # omegaEO=PointMatIn[5,4]
   # phiEO  =PointMatIn[5,5]
   # kappaEO=PointMatIn[5,6]

print('calc A-Matrix x-equations')
R=rotMat.RyprG(PointMatIn[5,6],PointMatIn[5,5],PointMatIn[5,4])
a= math.sin(PointMatIn[5,6]*np.pi/200.0)
b= math.cos(PointMatIn[5,5]*np.pi/200.0)
c= math.cos(PointMatIn[5,4]*np.pi/200.0)
d= math.sin(PointMatIn[5,4]*np.pi/200.0)
e= math.cos(PointMatIn[5,6]*np.pi/200.0)
f= math.sin(PointMatIn[5,5]*np.pi/200.0)

rho2=np.dot(PointMatIn[1,1:4],PointMatIn[1,1:4])

#dx/d_X0  dx/d_Y0  dx/d_Z0
PointMatIn[1,11:14]=[ - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[0,2]*PointMatIn[1,6] - R[0,0]*PointMatIn[1,8]),
                      - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[1,2]*PointMatIn[1,6] - R[1,0]*PointMatIn[1,8]), 
                      - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[2,2]*PointMatIn[1,6] - R[2,0]*PointMatIn[1,8]) ]

PointMatIn[2,11:14]=[ - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[0,2]*PointMatIn[2,6] - R[0,0]*PointMatIn[2,8]),
                      - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[1,2]*PointMatIn[2,6] - R[1,0]*PointMatIn[2,8]), 
                      - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[2,2]*PointMatIn[2,6] - R[2,0]*PointMatIn[2,8]) ]

PointMatIn[3,11:14]=[ - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[0,2]*PointMatIn[3,6] - R[0,0]*PointMatIn[3,8]),
                      - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[1,2]*PointMatIn[3,6] - R[1,0]*PointMatIn[3,8]), 
                      - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[2,2]*PointMatIn[3,6] - R[2,0]*PointMatIn[3,8]) ]

PointMatIn[4,11:14]=[ - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[0,2]*PointMatIn[4,6] - R[0,0]*PointMatIn[4,8]),
                      - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[1,2]*PointMatIn[4,6] - R[1,0]*PointMatIn[4,8]), 
                      - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[2,2]*PointMatIn[4,6] - R[2,0]*PointMatIn[4,8]) ]

#dx/d_omega  dx/d_phi  dx/d_kappa
PointMatIn[1,14:17]=[ - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(PointMatIn[1,1]*PointMatIn[1,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[1,7])/(PointMatIn[1,8]**2)*(c*PointMatIn[1,2]+d*PointMatIn[1,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[1,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[1,7])/(PointMatIn[1,8]**2)*(f*PointMatIn[1,1] - d*b*PointMatIn[1,2] + c*b*PointMatIn[1,3] )  ]
    
PointMatIn[2,14:17]=[ - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(PointMatIn[2,1]*PointMatIn[2,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[2,7])/(PointMatIn[2,8]**2)*(c*PointMatIn[2,2]+d*PointMatIn[2,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[2,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[2,7])/(PointMatIn[2,8]**2)*(f*PointMatIn[2,1] - d*b*PointMatIn[2,2] + c*b*PointMatIn[2,3] )  ]

PointMatIn[3,14:17]=[ - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(PointMatIn[3,1]*PointMatIn[3,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[3,7])/(PointMatIn[3,8]**2)*(c*PointMatIn[3,2]+d*PointMatIn[3,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[3,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[3,7])/(PointMatIn[3,8]**2)*(f*PointMatIn[3,1] - d*b*PointMatIn[3,2] + c*b*PointMatIn[3,3] )  ]

PointMatIn[4,14:17]=[ - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(PointMatIn[4,1]*PointMatIn[4,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[4,7])/(PointMatIn[4,8]**2)*(c*PointMatIn[4,2]+d*PointMatIn[4,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[4,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[4,7])/(PointMatIn[4,8]**2)*(f*PointMatIn[4,1] - d*b*PointMatIn[4,2] + c*b*PointMatIn[4,3] )  ]



#dy/d_X0  dy/d_Y0  dy/d_Z0
PointMatIn[1,17:20]=[ - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[0,2]*PointMatIn[1,7] - R[0,0]*PointMatIn[1,8]),
                      - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[1,2]*PointMatIn[1,7] - R[1,0]*PointMatIn[1,8]), 
                      - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(R[2,2]*PointMatIn[1,7] - R[2,0]*PointMatIn[1,8]) ]

PointMatIn[2,17:20]=[ - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[0,2]*PointMatIn[2,7] - R[0,0]*PointMatIn[2,8]),
                      - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[1,2]*PointMatIn[2,7] - R[1,0]*PointMatIn[2,8]), 
                      - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(R[2,2]*PointMatIn[2,7] - R[2,0]*PointMatIn[2,8]) ]

PointMatIn[3,17:20]=[ - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[0,2]*PointMatIn[3,7] - R[0,0]*PointMatIn[3,8]),
                      - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[1,2]*PointMatIn[3,7] - R[1,0]*PointMatIn[3,8]), 
                      - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(R[2,2]*PointMatIn[3,7] - R[2,0]*PointMatIn[3,8]) ]

PointMatIn[4,17:20]=[ - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[0,2]*PointMatIn[4,7] - R[0,0]*PointMatIn[4,8]),
                      - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[1,2]*PointMatIn[4,7] - R[1,0]*PointMatIn[4,8]), 
                      - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(R[2,2]*PointMatIn[4,7] - R[2,0]*PointMatIn[4,8]) ]



#dy/d_omega  dy/d_phi  dy/d_kappa
PointMatIn[1,20:23]=[  PointMatIn[0,0]/(PointMatIn[1,8]**2)*(PointMatIn[1,1]*PointMatIn[1,6] + rho2*e*b  ),
                       (PointMatIn[0,0]*PointMatIn[1,6])/(PointMatIn[1,8]**2)*(c*PointMatIn[1,2]+d*PointMatIn[1,3]) - rho2*a*PointMatIn[0,0]/(PointMatIn[1,8]**2),
                       (PointMatIn[0,0]*PointMatIn[1,6])/(PointMatIn[1,8]**2)*(f*PointMatIn[1,1] - d*b*PointMatIn[1,2] + c*b*PointMatIn[1,3] )  ]
    
PointMatIn[2,20:23]=[  PointMatIn[0,0]/(PointMatIn[2,8]**2)*(PointMatIn[2,1]*PointMatIn[2,6] + rho2*e*b  ),
                       (PointMatIn[0,0]*PointMatIn[2,6])/(PointMatIn[2,8]**2)*(c*PointMatIn[2,2]+d*PointMatIn[2,3]) - rho2*a*PointMatIn[0,0]/(PointMatIn[2,8]**2),
                       (PointMatIn[0,0]*PointMatIn[2,6])/(PointMatIn[2,8]**2)*(f*PointMatIn[2,1] - d*b*PointMatIn[2,2] + c*b*PointMatIn[2,3] )  ]

PointMatIn[3,20:23]=[  PointMatIn[0,0]/(PointMatIn[3,8]**2)*(PointMatIn[3,1]*PointMatIn[3,6] + rho2*e*b  ),
                       (PointMatIn[0,0]*PointMatIn[3,6])/(PointMatIn[3,8]**2)*(c*PointMatIn[3,2]+d*PointMatIn[3,3]) - rho2*a*PointMatIn[0,0]/(PointMatIn[3,8]**2),
                       (PointMatIn[0,0]*PointMatIn[3,6])/(PointMatIn[3,8]**2)*(f*PointMatIn[3,1] - d*b*PointMatIn[3,2] + c*b*PointMatIn[3,3] )  ]

PointMatIn[4,20:23]=[  PointMatIn[0,0]/(PointMatIn[4,8]**2)*(PointMatIn[4,1]*PointMatIn[4,6] + rho2*e*b  ),
                       (PointMatIn[0,0]*PointMatIn[4,6])/(PointMatIn[4,8]**2)*(c*PointMatIn[4,2]+d*PointMatIn[4,3]) - rho2*a*PointMatIn[0,0]/(PointMatIn[4,8]**2),
                       (PointMatIn[0,0]*PointMatIn[4,6])/(PointMatIn[4,8]**2)*(f*PointMatIn[4,1] - d*b*PointMatIn[4,2] + c*b*PointMatIn[4,3] )  ]


    

    
    
    
   # return Alger