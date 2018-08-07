import numpy as np

def Rypr(y, p, r):
    
    # Rotation Matrix for y = yaw (Z-Axis) p = pitch (Y-Axis) and r = roll (X-Axis)
    # from Degree to Radians
    y = y*np.pi/180.0
    p = p*np.pi/180.0
    r = r*np.pi/180.0
 
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
 
    return Ry*Rp*Rr

def RyprG(y, p, r):
    #Kappa,Phi,Omega
    # Rotation Matrix for y = yaw (Z-Axis) p = pitch (Y-Axis) and r = roll (X-Axis)
    # from Gon to Radians
    
    #Omega – Rotation about the X axis
    #Phi – Rotation about the Y axis
    #Kappa – Rotation about the Z axis

    #
    #y = y*np.pi/200.0
    #p = p*np.pi/200.0
    #r = r*np.pi/200.0
 
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
 
    return Ry*Rp*Rr




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