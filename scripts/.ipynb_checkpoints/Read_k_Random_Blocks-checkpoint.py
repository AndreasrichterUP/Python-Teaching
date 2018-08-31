

def Read_k_Random_Blocks(number, Ordner):
    import numpy as np
    import scipy.io as sio
    # number :    Anzahl der Bloecke, die gelesen und zusammengefuegt werden sollen
    # Ordner :    Pfad zu den Kacheln (Bloecken) als *.mat files
    A_Train=np.ones((1,21))
    
    RBlockNrs=np.array([6])   # sicherstellen das beide Klassen in den Daten vorhanden sind!!!
    nums=np.random.choice(39,number,replace=False)
    nums=nums+1
    id6= (nums == 6)
    nums[id6]= 40
    RBlockNrs=np.concatenate((RBlockNrs,nums), axis=0)
    
    
    print( RBlockNrs)
    for i in RBlockNrs:
        if i <= 9:
            name=Ordner+'/Matrix_A_Tile_0'+str(i)+".mat"
        else:
            name=Ordner+'/Matrix_A_Tile_'+str(i)+".mat"
       
    
        Train_Data1=sio.loadmat(name)                                        # lesen eines Blocks
        A_Train=np.concatenate((A_Train,Train_Data1.get('A_Train')), axis=0) # Anhaengen des Blocks an die letzte Zeile


    A_Train=np.delete(A_Train,0,0)  # loeschen der ersten Zeile in der A-Matrix 
    #print A_Train.shape
    
    
    return A_Train