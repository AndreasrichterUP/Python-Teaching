import numpy as np
import math

def Rypr(y, p, r):
    #Omega – Rotation around the X-axis .... (r)oll
    #Phi – Rotation around the Y-axis....... (p)itch
    #Kappa – Rotation around the Z-axis..... (y)aw

    # Rotation Matrix for y = yaw (Z-Axis) p = pitch (Y-Axis) and r = roll (X-Axis)
    # from Degree to Radians
    y = y*np.pi/180.0
    p = p*np.pi/180.0
    r = r*np.pi/180.0
 
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
    
    return np.dot(np.dot(Ry,Rp),Rr)
    #return Ry*Rp*Rr

def RyprG(y, p, r):
    #Kappa,Phi,Omega
    # Rotation Matrix for y = yaw (Kappa, Z-Axis) p = pitch (Phi, Y-Axis) and r = roll (Omega ,X-Axis)
    # from Gon to Radians
    
    #Omega – Rotation around the X axis
    #Phi – Rotation around the Y axis
    #Kappa – Rotation around the Z axis

    # from Gon to Radiants
    #y = y*np.pi/200.0
    #p = p*np.pi/200.0
    #r = r*np.pi/200.0
 
    #Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    #Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    #Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])

    Rr = np.array([[1.0, 0.0, 0.0],[0.0, math.cos(r), -math.sin(r)],[0.0, math.sin(r), math.cos(r)]])
    Rp = np.array([[math.cos(p), 0.0, math.sin(p)],[0.0, 1.0, 0.0],[-math.sin(p), 0.0, math.cos(p)]])
    Ry = np.array([[math.cos(y), -math.sin(y), 0.0],[math.sin(y), math.cos(y), 0.0],[0.0, 0.0, 1.0]])

    kappaEO=y
    phiEO  =p
    omegaEO=r
    
    #r11= math.cos(phiEO)*math.cos(kappaEO);
    #r12=-math.cos(phiEO)*math.sin(kappaEO);
    #r13= math.sin(phiEO);

    #r21= math.cos(omegaEO)*math.sin(kappaEO)+math.sin(omegaEO)*math.sin(phiEO)*math.cos(kappaEO);
    #r22= math.cos(omegaEO)*math.cos(kappaEO)-math.sin(omegaEO)*math.sin(phiEO)*math.sin(kappaEO);
    #r23=-math.sin(omegaEO)*math.cos(phiEO);

    #r31= math.sin(omegaEO)*math.sin(kappaEO)-math.cos(omegaEO)*math.sin(phiEO)*math.cos(kappaEO);
    #r32= math.sin(omegaEO)*math.cos(kappaEO)+math.cos(omegaEO)*math.sin(phiEO)*math.sin(kappaEO);
    #r33= math.cos(omegaEO)*math.cos(phiEO);
    
    R1=np.dot(np.dot(Ry,Rp),Rr)
    #R2=np.array([[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]])

    return R1
    #return Rr,Rp,Ry
    #return np.dot(np.dot(Ry,Rp),Rr)
    #return Ry*Rp*Rr




def QtoR(q):
    #Calculates the Rotation Matrix from Quaternion
    #a is the real part
    #b, c, d are the complex elements
    # Source: Buchholz, J. J. (2013). Vorlesungsmanuskript Regelungstechnik und Flugregler.
    # GRIN Verlag. Retrieved from http://www.grin.com/de/e-book/82818/regelungstechnik-und-flugregler
    #q = normQ(q)
 
    a, b, c, d = q
 
    R11 = (a**2+b**2-c**2-d**2)
    R12 = 2.0*(b*c-a*d)
    R13 = 2.0*(b*d+a*c)
 
    R21 = 2.0*(b*c+a*d)
    R22 = a**2-b**2+c**2-d**2
    R23 = 2.0*(c*d-a*b)
 
    R31 = 2.0*(b*d-a*c)
    R32 = 2.0*(c*d+a*b)
    R33 = a**2-b**2-c**2+d**2
 
    return np.matrix([[R11, R12, R13],[R21, R22, R23],[R31, R32, R33]])