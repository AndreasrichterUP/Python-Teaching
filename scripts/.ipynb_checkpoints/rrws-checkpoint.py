
# Class to save a point with number, image coordinates (xI,yI) and 
# world coordinates (Xw Yw Zw) 
class Point:
    def __init__(self, No,Xw,Yw,Zw,xI,yI):
        self.No,self.Xw,self.Yw, self.Zw, self.xI, self.yI = No,Xw,Yw,Zw,xI, yI

  # function to add two points      
    def add(self, other):
        return Point(self.No,self.Xw + other.Xw,self.Yw + other.Yw,self.Zw + other.Zw,self.xI + other.xI, self.yI + other.yI)

  # function to calc the difference of world coordinates of two points  
    def subtr(self, other):
        return Point(self.No,self.Xw - other.Xw,self.Yw - other.Yw,self.Zw - other.Zw,self.xI, self.yI)
  
  # function to print the point with all its attributes
    def println(self):
        print("( {}, {},{}, {}, {}, {})".format(self.No ,self.Xw, self.Yw, self.Zw, self.xI, self.yI))

        
  # test of the functions      
if __name__ == '__main__':
    p1 = Point(5, 1361.29,  -1402.17,  200,   0.110,   0.110,)
    p2 = Point(6, 1337.27,  -1019.37,  210,   0.080,   0.110,)
    p1.println()
    p2.println()
    p1.add(p2).println()
    #sys.exit(0)
###



# function to do the iterational steps of the ajustment process
# Inputs are the known points (GCP) and the Rotation Matrix
def calcDifferentials(PointMatIn,R):
    import numpy as np
    import math
    
    print('Input Array has Dims: {} '.format(PointMatIn.shape))
    print('calc deltas of Points')
    
    # the delta points are used in all the following equations
    # Point 5 is the focus-center of the Camera (XYZ) and the other points are the world   
    # coordinates (exterior coordinates XYZ) of the meassured ground controll points 
    # (GCP's)
    # The relative coordinates (point differences) are used in the kollinearity equations
    PointMatIn[1,1:4]=PointMatIn[1,1:4]-PointMatIn[5,1:4]
    PointMatIn[2,1:4]=PointMatIn[2,1:4]-PointMatIn[5,1:4]
    PointMatIn[3,1:4]=PointMatIn[3,1:4]-PointMatIn[5,1:4]
    PointMatIn[4,1:4]=PointMatIn[4,1:4]-PointMatIn[5,1:4]
    
    # the index of the rows [1,1:4] (here the first number 1) represents a GCP Point

    
    
    
    print('===========================')
    #print(PointMatIn)

    print('calc U, V and W')
    # These are helping Variables for the cal of the collinearity equations
    # U....Zaehler/Counter of the equation in respect to x
    # V....Zaehler/Counter of the equation in respect to y
    # W....Nenner/Number of both equations
    
    # Index [1,6:9] here the second index represents a variable according to
    #U....index:6
    #V....index:7
    #W....index:8

    # U[i]= r11*dX[i]+r21*dY[i]+r31*dZ[i];
	# V[i]= r12*dX[i]+r22*dY[i]+r32*dZ[i];
	# W[i]= r13*dX[i]+r23*dY[i]+r33*dZ[i];

    
    
    # The Values for UVW are dependent on the Rotation Matrix and the Point Differences
    PointMatIn[1,6:9]=np.dot(R.T,PointMatIn[1,1:4])
    PointMatIn[2,6:9]=np.dot(R.T,PointMatIn[2,1:4])
    PointMatIn[3,6:9]=np.dot(R.T,PointMatIn[3,1:4])
    PointMatIn[4,6:9]=np.dot(R.T,PointMatIn[4,1:4])
    # By the index 6:9 the fields 6,7 and 8 are calculated
    # For every row the Values of U,V,W are calculated
    # because the values change depending on the points coordinates 
    
    print('===========================')
    #print(PointMatIn)

    print('calc lger')
    
    # The following equations calculate values of the observations for x' and y' depending on the values of U V W
    # for example PointMatIn[1,6] = U  PointMatIn[1,7]= V  and  PointMatIn[1,8] = W
    # based on the given geometry, U V and W itself depend on the GCPs and their spatial relationships   
    
    # PointMatIn[0,0] is the camera constant c of the interior orientation
    # PointMatIn[0,1] is the projection center x0IO of the interior orientation
    # PointMatIn[0,2] is the projection center y0IO of the interior orientation
    
    # x0IO - c*(U/W)
    # y0IO - c*(V/W)
    
    # The matrix structure is extended by the cols [1,9] and [1,10]
    # check the following equations compare "Krauss, Photogrammetie Vol 1"
  
    PointMatIn[1,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[1,6]/PointMatIn[1,8], PointMatIn[0,2] -       PointMatIn[0,0]*PointMatIn[1,7]/PointMatIn[1,8] ]

    PointMatIn[2,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[2,6]/PointMatIn[2,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[2,7]/PointMatIn[2,8] ]

    PointMatIn[3,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[3,6]/PointMatIn[3,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[3,7]/PointMatIn[3,8] ]

    PointMatIn[4,9:11]=[ PointMatIn[0,1] - PointMatIn[0,0]*PointMatIn[4,6]/PointMatIn[4,8], PointMatIn[0,2] - PointMatIn[0,0]*PointMatIn[4,7]/PointMatIn[4,8] ]

   # omegaEO=PointMatIn[5,4]
   # phiEO  =PointMatIn[5,5]
   # kappaEO=PointMatIn[5,6]

    print('calc A-Matrix x-equations')
    
    # The so called A-Matrix stores the differentials according to every variable in the collinearity equations
    
    a= math.sin(PointMatIn[5,6])   # sin(kappa)
    b= math.cos(PointMatIn[5,5])   # cos(phi) 
    c= math.cos(PointMatIn[5,4])   # cos(omega)
    d= math.sin(PointMatIn[5,4])   # sin(omega)
    e= math.cos(PointMatIn[5,6])   # cos(kappa)
    f= math.sin(PointMatIn[5,5])   # sin(phi)

    #rho2=np.dot(PointMatIn[1,1:4],PointMatIn[1,1:4])
    # X*X + Y*Y + Z*Z ???
    
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
    rho2=np.dot(PointMatIn[1,1:4],PointMatIn[1,1:4])
    PointMatIn[1,14:17]=[ - PointMatIn[0,0]/(PointMatIn[1,8]**2)*(PointMatIn[1,1]*PointMatIn[1,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[1,7])/(PointMatIn[1,8]**2)*(c*PointMatIn[1,2]+d*PointMatIn[1,3]) +      rho2*e*PointMatIn[0,0]/(PointMatIn[1,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[1,7])/(PointMatIn[1,8]**2)*(f*PointMatIn[1,1] - d*b*PointMatIn[1,2] +   c*b*PointMatIn[1,3] )  ]
    
    rho2=np.dot(PointMatIn[2,1:4],PointMatIn[2,1:4])
    PointMatIn[2,14:17]=[ - PointMatIn[0,0]/(PointMatIn[2,8]**2)*(PointMatIn[2,1]*PointMatIn[2,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[2,7])/(PointMatIn[2,8]**2)*(c*PointMatIn[2,2]+d*PointMatIn[2,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[2,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[2,7])/(PointMatIn[2,8]**2)*(f*PointMatIn[2,1] - d*b*PointMatIn[2,2] + c*b*PointMatIn[2,3] )  ]

    rho2=np.dot(PointMatIn[3,1:4],PointMatIn[3,1:4])
    PointMatIn[3,14:17]=[ - PointMatIn[0,0]/(PointMatIn[3,8]**2)*(PointMatIn[3,1]*PointMatIn[3,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[3,7])/(PointMatIn[3,8]**2)*(c*PointMatIn[3,2]+d*PointMatIn[3,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[3,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[3,7])/(PointMatIn[3,8]**2)*(f*PointMatIn[3,1] - d*b*PointMatIn[3,2] + c*b*PointMatIn[3,3] )  ]

    rho2=np.dot(PointMatIn[4,1:4],PointMatIn[4,1:4])
    PointMatIn[4,14:17]=[ - PointMatIn[0,0]/(PointMatIn[4,8]**2)*(PointMatIn[4,1]*PointMatIn[4,7] + rho2*a*b  ),
                      - (PointMatIn[0,0]*PointMatIn[4,7])/(PointMatIn[4,8]**2)*(c*PointMatIn[4,2]+d*PointMatIn[4,3]) + rho2*e*PointMatIn[0,0]/(PointMatIn[4,8]**2),
                      - (PointMatIn[0,0]*PointMatIn[4,7])/(PointMatIn[4,8]**2)*(f*PointMatIn[4,1] - d*b*PointMatIn[4,2] + c*b*PointMatIn[4,3] )  ]


    print('calc A-Matrix y-equations')
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

    #print(PointMatIn)
    Alger=PointMatIn    
    return Alger




# Matrix Structure Used for Calculations

#   [[  0 , 1, 2, 3, 4, 5, 6, 7, 8,  9   ,  10  ,   11  ,   12   ,  13   ,  14      ,  15    ,   16     ,   17  ,   18  ,  19   ,   20,    ,   21   ,   22 ]
#  1 [ Pnr,dx,dy,dz,xI,yI, U, V, W,xIcalc,yIcalc,dx/d_X0, dx/d_Y0,dx/d_Z0,dx/d_omega,dx/d_phi,dx/d_kappa,dy/d_X0,dy/d_Y0,dy/d_Z0,dy/d_omega,dy/d_phi,dy/d_kappa      ]
#  2 [ ...] 
#  3 [ ...]
#  4 [ ...]
#  5 [ ...]
#  6 [ ...] 

#PointMatIn[0,:]=[c,x0IO,y0IO,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#PointMatIn[1,:]=[1,    1361.29,  -1402.17,       200,   0.110,   0.110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#PointMatIn[2,:]=[2,    1038.53,    1026.25,      500,  -0.110,   0.110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#PointMatIn[3,:]=[3,   -1253.46,    1139.02,      300,  -0.110,  -0.110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#PointMatIn[4,:]=[4,   -1325.27,   -1421.83,      250,   0.110,  -0.110,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#PointMatIn[5,:]=[0,      1.132,      1.132, 2002.264,  omegaEO,  phiEO,kappaEO,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
