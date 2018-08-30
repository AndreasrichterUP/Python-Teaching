def Dict2DesignMatrix(LayerDict):
    
    # Input: function takes a dictionary of rasterlayers as input
    # Output: a predictor Matrix containing number of rows equal to all Pixels of one rasterlayer and columns equal to all layers 
    #         in the Dictionary 
    
    
    # Function iterates through all layers of the dict
    # checks if it is a layer with nominal data [0,1] (TIF_n) or a layer with rational data  (TIF_r, floating point numbers)
    
    # for rational layers a min max normalization is applied to get numbers between 0,...,1. ; rastermatrix is reshaped to a 
    # column vector and assigned to a column in the predictor Matrix 
    
    # for nominal data layers same procedure is applied, but without min max normalization
    
    import numpy as np
    ncols=len(LayerDict)+1 
    #print ncols
    A=np.zeros((np.ravel(LayerDict.itervalues().next()).shape[0],ncols))  #Design Matrix Speicher initialisieren
    #print A.shape
    A[:,0] = 1.0
    i=1
    #print 'Spalte A[:,{}], Name: Ones  shape :{}'.format(0, np.ravel( A[:,0]).shape)
    
                                                         
    for layer in sorted(LayerDict): 
                                                         
        if 'TIF_r' in layer :
            a=np.max(np.ravel(LayerDict.get(layer)))
            b=np.min(np.ravel(LayerDict.get(layer)))
            
            A[:,i] =  (np.ravel(LayerDict.get(layer)) - b)/ (a-b)       #         =Mat2NormVec( LayerDict.get(layer))
            #print i, layer, np.ravel(LayerDict.get(layer)).shape
            #print 'Spalte A[:,{}], Name:{}  shape :{}'.format(i, layer, np.ravel(LayerDict.get(layer)).shape)
        elif 'TIF_n' in layer :
            A[:,i]=np.ravel(LayerDict.get(layer))    #=  Mat2Vec( LayerDict.get(layer))
            #print i, layer, np.ravel(LayerDict.get(layer)).shape
            #print 'Spalte A[:,{}], Name:{}  shape :{}'.format(i, layer, np.ravel(LayerDict.get(layer)).shape)
        else: 
            i-=1
            A[:,ncols-1]=np.ravel(LayerDict.get(layer))          # = Mat2Vec(LayerDict.get('TIF_TrueLabels'))
            #print 'Spalte A[:,{}], Name:{}  shape :{}'.format(ncols-1, layer, np.ravel(LayerDict.get(layer)).shape)
            
        i+=1
    #
    return A