def ReadRasters2Dict(Folder):
    # https://docs.python.org/2/library/glob.html 
    # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    import glob
    import skimage.io as skio
    import numpy as np
    #Folder='../../_Data_ori_Tif/AOI3_V7_Train/'
    #Folder='../../_Data_ori_Tif/AOI2_small_6_Test/'
    TIFs=glob.glob(Folder+"*.tif")
    #PNGs=glob.glob(Folder+"*.png")
    #TFWs=glob.glob(Folder+"*.tfw")
    i=0
    LayerTrain=dict()
    for Tif in TIFs:
        print( Tif)
    print( '-----')
   
    
    for filr in TIFs:
                   
        if '_AS' in filr or '_L' in filr :
            #print i, filr.split("/")[4][0:4]+'n_'+filr.split("/")[4][4:-4]
            name=filr.split("/")[-1][0:4]+'n_'+filr.split("/")[-1][4:-4]
            print( name)
            LayerTrain[name]=np.float32(skio.imread(filr))
            print( LayerTrain[name].shape)
            print( 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1)))
            
            if '_Landcover' in filr:
                print( name)
                LayerTrain['TIF_n_LanduseRAL'] =np.float32(((LayerTrain.get(name) == 1) | (LayerTrain.get(name) ==5))*1.0)
                print( 'TIF_n_LanduseRAL ', LayerTrain['TIF_n_LanduseRAL'].shape  #Rainfed Agricultural Land....ok)
                LayerTrain['TIF_n_LanduseRL']  =np.float32(( LayerTrain.get(name) == 2)*1.0)
                print( 'TIF_n_LanduseRL ', LayerTrain['TIF_n_LanduseRL'].shape    #Range Land....ok)
                LayerTrain['TIF_n_LanduseIRA']=np.float32(((LayerTrain.get(name)==4)|(LayerTrain.get(name)==9)|      (LayerTrain.get(name)==10))*1.0)
                print( 'TIF_n_LanduseIRA ', LayerTrain['TIF_n_LanduseIRA'].shape  #Irrigated Agricultural Land....ok)
            
                # ----------------------------------------------- 
                #plt.imshow(TIF_lc93_32 ==3)                            #Sandcover, !!!!!nicht vorhanden
                #plt.imshow(TIF_lc93_32 ==6)  ==8) ==14)                # % Waterbody and Marshland !!!! nicht vorhanden
                # TIF_lc93_32==7)  % Fruit Trees.......... Fruchtbaeume)  !!!nicht vorhanden
                #plt.imshow(TIF_lc93_32 ==11,12,13)  % Vineyards  .......... Weinberge) % Forest and Shrubs ... !!!nicht vorhanden
                #plt.show()
            
                del LayerTrain[name] 
            if '_Lith' in filr:
                print( name)
                LayerTrain['TIF_n_VOLC'] =np.float32((LayerTrain.get(name) == 1)*1.0)  # % Volcanic ...... Vulkanisches Gestein
                print( 'TIF_n_VOLC ', LayerTrain['TIF_n_VOLC'].shape)
                LayerTrain['TIF_n_SEDI'] =np.float32((LayerTrain.get(name) == 2)*1.0)  # % Sedimentary ... Sedimente
                print( 'TIF_n_SEDI ', LayerTrain['TIF_n_SEDI'].shape)
                LayerTrain['TIF_n_PLUT'] =np.float32((LayerTrain.get(name) == 3)*1.0)  # % Plutonic....... Plutonisches Gestein
                print( 'TIF_n_SEDI ', LayerTrain['TIF_n_SEDI'].shape)

                #TIF_META= (TIF_lith_type == 4) # % Metamorphic.... Metamorphes Gestein .... nicht vorhanden!!!! 
                del LayerTrain[name]                   

        
        elif 'True' in filr : 
            
            #'_Tr' in filr:
            #print i, filr.split("/")[4][0:-4]
            name =filr.split("/")[-1][0:-4]
            print( name)
           
            LayerTrain[name]=np.float32(skio.imread(filr))
            print( 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1)))
            
            LayerTrain[name]=np.float32((LayerTrain.get(name) !=255)*1.0)             # TrueLabels auf Intervall [0,1] bringen
            print( LayerTrain[name].shape)
                      
        
        else:
            #print i, filr , filr.split("/")[4][0:4]+'r_'+filr.split("/")[4][4:-4]
            name=filr.split("/")[-1][0:4]+'r_'+filr.split("/")[-1][4:-4]
            print( name)
            
            if '_roads' in filr:
                LayerTrain[name]=np.float32(skio.imread(filr))
                LayerTrain[name]=LayerTrain[name][:,:-1]
            else:
                LayerTrain[name]=np.float32(skio.imread(filr))
            
            print( LayerTrain[name].shape)
            print( 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1)))
            
            
            
            
            
            if '_DistStreams' in filr or '_faults' in filr or '_roads' in filr or '_tak' in filr:
                print( name)
                LayerTrain[name]=np.log(LayerTrain[name])
                print( LayerTrain[name].shape)
                print( 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1)))
                print( 'Anzahl infty : {}'.format(np.sum(np.isinf(LayerTrain[name])*1)))
                LayerTrain[name][np.isinf(LayerTrain[name])]=0
                print( 'Wert infty durch 0 ersetzt / Anzahl infty jetzt: {}'.format(np.sum(np.isinf(LayerTrain[name])*1)))
     
        




        i+=1



    return LayerTrain