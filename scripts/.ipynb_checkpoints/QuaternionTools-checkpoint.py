import numpy as np
import math

def Q_normalize(array):
    #Normalize a 4 element array/list/numpy.array for use as a quaternion
    #:param quat_array: 4 element list/array
    #:returns: normalized array
    #:rtype: numpy array

  
    quat = np.array(array)
    return quat / np.sqrt(np.dot(quat, quat))



def Q_make(w,array):
    a=np.array(array)
    #print a
    q=np.array([np.cos((w*math.pi)/(2*180.0)),a[0]*np.sin((w*math.pi)/(2*180)),a[1]*np.sin((w*math.pi)/(2*180)),a[2]*np.sin((w*math.pi)/(2*180))])
    
    return q

#Einheitsquaternion erstellen
#q=np.array([ np.cos((60*math.pi)/(2*180)),0,0,-1*np.sin((60*math.pi)/(2*180)) ] )


def Q_inv(array):
    # array muss hier eine  Einheitsquaternion sein!!!
    iqE=-array
    iqE[0]=-iqE[0]
    return iqE


def Q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return np.array([w, x, y, z])  # liefert Array zurueck

def Q_conj(array):
    qCon=np.array([array[0],-array[1],-array[2],-array[3]])
    return qCon

def Q_rotateVector(axis,angle,vec):
    
    qE_Axis  = Q_normalize(Q_make(angle,axis))
    iqE_Axis = Q_conj(qE_Axis)
    q_vec    = np.append([0],vec)
    q_RotVec = Q_mult(Q_mult(qE_Axis,q_vec),iqE_Axis)
    RotVec   = np.array([q_RotVec[1],q_RotVec[2],q_RotVec[3]])
    return RotVec