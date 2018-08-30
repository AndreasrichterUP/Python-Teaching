
def ReadRaster2Dict(Folder):
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
        print Tif
    print '-----'
   
    
    for filr in TIFs:
    
        if '_GDEM' in filr or '_C' in filr or '_Di' in filr or '_E' in filr or '_Pre' in filr or '_S' in filr or '_N' in filr:
            #print i, filr , filr.split("/")[4][0:4]+'r_'+filr.split("/")[4][4:-4]
            name=filr.split("/")[4][0:4]+'r_'+filr.split("/")[4][4:-4]
            print name
            #LayerTrain[name]=np.float32(skio.imread(filr))
            #print LayerTrain[name].shape
            #print 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1))
            
            if '_DistStreams' in filr or '_faults' in filr or '_roads' in filr or '_tak' in filr:
                print name
                #LayerTrain[name]=np.log(LayerTrain[name])
                #print LayerTrain[name].shape
                #print 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1))
                #print 'Anzahl infty : {}'.format(np.sum(np.isinf(LayerTrain[name])*1))
                #LayerTrain[name][np.isinf(LayerTrain[name])]=0
                #print 'Wert infty durch 0 ersetzt / Anzahl infty jetzt: {}'.format(np.sum(np.isinf(LayerTrain[name])*1))
                
        elif '_AS' in filr or '_l' in filr :
            #print i, filr.split("/")[4][0:4]+'n_'+filr.split("/")[4][4:-4]
            name=filr.split("/")[4][0:4]+'n_'+filr.split("/")[4][4:-4]
            print name
            #LayerTrain[name]=np.float32(skio.imread(filr))
            #print LayerTrain[name].shape
            #print 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1))
            
            if '_Landcover' in filr:
                print name
                #LayerTrain['TIF_n_LanduseRAL'] =((LayerTrain.get(name) == 1) | (LayerTrain.get(name) ==5))*1.0
                #print 'TIF_n_LanduseRAL ', LayerTrain['TIF_n_LanduseRAL'].shape  #Rainfed Agricultural Land....ok
                #LayerTrain['TIF_n_LanduseRL']  =( LayerTrain.get(name) == 2)*1.0
                #print 'TIF_n_LanduseRL ', LayerTrain['TIF_n_LanduseRL'].shape    #Range Land....ok
                #LayerTrain['TIF_n_LanduseIRA']=((LayerTrain.get(name)==4)|(LayerTrain.get(name)==9)|      (LayerTrain.get(name)==10))*1.0
                #print 'TIF_n_LanduseIRA ', LayerTrain['TIF_n_LanduseIRA'].shape  #Irrigated Agricultural Land....ok
            
                # ----------------------------------------------- 
                #plt.imshow(TIF_lc93_32 ==3)                            #Sandcover, !!!!!nicht vorhanden
                #plt.imshow(TIF_lc93_32 ==6)  ==8) ==14)                # % Waterbody and Marshland !!!! nicht vorhanden
                # TIF_lc93_32==7)  % Fruit Trees.......... Fruchtbaeume)  !!!nicht vorhanden
                #plt.imshow(TIF_lc93_32 ==11,12,13)  % Vineyards  .......... Weinberge) % Forest and Shrubs ... !!!nicht vorhanden
                #plt.show()
            
                #del LayerTrain[name] 
            if '_Lith' in filr:
                print name
                #LayerTrain['TIF_n_VOLC'] =(LayerTrain.get(name) == 1)*1.0  # % Volcanic ...... Vulkanisches Gestein
                #print 'TIF_n_VOLC ', LayerTrain['TIF_n_VOLC'].shape
                #LayerTrain['TIF_n_SEDI'] =(LayerTrain.get(name) == 2)*1.0  # % Sedimentary ... Sedimente
                #print 'TIF_n_SEDI ', LayerTrain['TIF_n_SEDI'].shape
                #LayerTrain['TIF_n_PLUT'] =(LayerTrain.get(name) == 3)*1.0  # % Plutonic....... Plutonisches Gestein
                #print 'TIF_n_SEDI ', LayerTrain['TIF_n_SEDI'].shape

                #TIF_META= (TIF_lith_type == 4) # % Metamorphic.... Metamorphes Gestein .... nicht vorhanden!!!! 
                #del LayerTrain[name]                   


        elif '_Tr' in filr:
            #print i, filr.split("/")[4][0:-4]
            name =filr.split("/")[4][0:-4]
            print name
            #LayerTrain[name]=np.float32(skio.imread(filr))
            #LayerTrain[name]=(LayerTrain.get(name) > 0)*1.0             # TrueLabels auf Intervall [0,1] bringen
            #print LayerTrain[name].shape
            #print 'Anzahl NaN : {}'.format(np.sum(np.isnan(LayerTrain[name])*1))           
        i+=1



    #return LayerTrain






def AlignAllRaster(LayerDict):
    # Ausschneiden und auf die gleiche Groesse bringen
    a,b =LayerDict['TIF_TrueLabels'].shape 
    print a,b


    for layer in sorted(LayerDict.keys()  ) :
        if  'TIF_r' in layer or 'TIF_n' in layer:
            print layer
            LayerDict[layer]=LayerDict.get(layer)[0:a,1:b]
            print LayerDict.get(layer).shape
        #else :
        #    print '---'
        #    print layer    
        #    LayerTrain[layer]=LayerTrain.get(layer)[:,1:]
        #    print LayerTrain.get(layer).shape


    #print sorted(LayerTrain.keys()  )
    print 'TIF_TrueLabels shape'  ,LayerDict['TIF_TrueLabels'].shape   
    print 'beheben'
    LayerDict['TIF_TrueLabels']=LayerDict.get('TIF_TrueLabels')[:,1:]
    print 'TIF_TrueLabels shape' , LayerDict.get('TIF_TrueLabels').shape

    return LayerDict




def Dict2DesignMatrix(LayerDict):
    from BasisFunctions import Mat2NormVec,Mat2Vec
    import numpy as np
    ncols=len(LayerDict)+1 
    print ncols
    A=np.zeros((np.ravel(LayerDict.get('TIF_TrueLabels')).shape[0],ncols))  #Design Matrix Speicher initialisieren

    A[:,0] = 1.0
    i=1

    for layer in sorted(LayerDict):
        if 'TIF_r' in layer :
            #A[:,i]=Mat2NormVec( LayerDict.get(layer))
            print i, layer, np.ravel(LayerDict.get(layer)).shape
        elif 'TIF_n' in layer :
            #A[:,i]=Mat2Vec( LayerDict.get(layer))
            print i, layer, np.ravel(LayerDict.get(layer)).shape

        else: 
            i-=1
            print i, layer, np.ravel(LayerDict.get(layer)).shape
        i+=1
    #A[:,ncols-1]=Mat2Vec(LayerDict.get('TIF_TrueLabels'))
    return A