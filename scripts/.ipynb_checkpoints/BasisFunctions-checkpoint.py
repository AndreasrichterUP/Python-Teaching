#%matplotlib inline
    

def plot_learningCurve(examplesLin,rocValues_Mean,rocValues_Var):
    #plt.figure()
    plt.title('Lernkurve')
    plt.xlabel('Anzahl der Trainingsbeispiele')
    plt.ylabel('AUC Wert')

    # error bars anzeigen lassen!!!
    plt.ylim([0.3, 1])
    #plt.xlim([1000, 150000])
    plt.grid()
    plt.fill_between(examplesLin, rocValues_Mean - 3*np.sqrt(rocValues_Var),rocValues_Mean + 3*np.sqrt(rocValues_Var), alpha=0.3,color="r")
    plt.plot(examplesLin,rocValues_Mean,label='LogReg (linear) ')

    plt.legend(loc="best")
    plt.show()
        
# Funktion zum Reshape
def Mat2Vec(Mat):
    import numpy as np
    Vec=np.ravel(Mat)
    #print(Vec.shape)
    return Vec

# Funktion zum Reshape einer Matrix in einen Vektor + Normierung der Werte auf Intervall [0,1]
def Mat2NormVec(Mat):
    import numpy as np
    Vec=np.ravel(Mat)
    #print(Vec.shape)
    a=np.max(Vec)
    b=np.min(Vec)
    NormVec= (Vec - b)/(a-b)
    return NormVec

# Funktion zum Normalisieren einer Matrix, Werte auf Intervall [0,1] bringen
def Mat2NormValue(Mat):
    #print( Mat.shape)
    a=np.max(Mat)
    b=np.min(Mat)
    NormMat= (Mat - b)/(a-b)
    return NormMat

# Funktion zur Ausgabe eines Bildes (Matrix) zusammen mit dem Histogramm
def showImage(Image):
    import numpy as np
    import matplotlib.pyplot as plt
    
    hist, bins = np.histogram(Image, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    
    # Two subplots, the axes array is 1-d
    fig=plt.figure(figsize=(20,8) )
    ax1 = fig.add_subplot(121)
    ax1.imshow(Image)
    ax1.set_title('Image')
    ax2 = fig.add_subplot(122)
    ax2.bar(center, hist, align='center', width=width)
    ax2.set_title('Histogramm')

    plt.show()
    
    
    
    
    
#helpful functions
#-------------------------------------------------------
# helper to plot ROC curves
def plot_roc_curves(fprs, tprs):
    fig = plt.figure(figsize=(20,10))
    for fpr, tpr in zip(fprs, tprs):
        plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc(fpr, tpr))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()

#-------------------------------------------------------
# The following function is a little visualization helper that draws the values 
# of the decision function on a heat map given a matplotlib axe
# wichtig an Daten anpassen, wird so nicht einfach funktionieren!
def show_decision_function(clf, ax):
    xx, yy = np.meshgrid(np.linspace(4.5, 8, 200), np.linspace(1.5, 4.0, 200))
    try:
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    except AttributeError:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 0]

    Z = Z.reshape(xx.shape)
    ax.pcolormesh(xx, yy, Z, cmap=plt.cm.jet)
    ax.set_xlim(4.5, 8)
    ax.set_ylim(1.5, 4.0)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, s=100)
    
    
    
    
def CutLayers2Subset(x,y,n,Ebenen):
    #   x,y : coordinates , numer of x=rows/ y=cols of upper left Corner
    #     n : length in hight width of the squared area around center point
    # Ebenen: Dictionary with all the layers
    import copy
    #http://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
    newEbenen=copy.deepcopy(Ebenen)
    print( 'Dim: {}'.format(n))
    print( 'Rows Start: {}   End: {}'.format(x,x+n))
    print( 'Cols Start: {}   End: {}'.format(y,y+n))
    
    for layer in sorted(newEbenen):
        if  '__' not in layer :
            #print( layer)
            newEbenen[layer]=newEbenen.get(layer)[x:x+n,y:y+n]
            #print( newEbenen.get(layer).shape)
    return newEbenen





def makeDesignMatrix(Ebenen):
    import numpy as np
    #Design Matrix Speicher allokieren
    ncols=len(Ebenen)-2               # -3 wegen [__globals__, __header__, __version__] +1 wegen 1stCol = 1.0 
    
    print( np.ravel(Ebenen.get('TrueLabels')).shape[0])
    print( '70% : ', np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7)
    print( '30% : ', np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.3)
    A=np.zeros((np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7),ncols))
    B=np.zeros((np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.3),ncols))
    c=(np.ravel(Ebenen.get('TrueLabels')).shape[0])-(np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7))
    print(c)
    
                                                     #32 ... dynamisch machen, Anzahl der Ebenen im dict() zaehlen
    A[:,0] = 1.0  # konstantes Attribut 
    B[:,0] = 1.0
    i=1
    print(A.shape)
    print(B.shape)

    #reshape Matrix in Vektor umwandeln
    for layer in sorted(Ebenen):
        #print(i)
        if 'TIF_r' in layer :
            Ebenen[layer]=Mat2NormVec( Ebenen.get(layer))
            #print( layer, Ebenen.get(layer).shape,np.min(Ebenen.get(layer)),np.max(Ebenen.get(layer)))
            A[:,i]=Ebenen.get(layer)[ : np.ceil(np.ravel(Ebenen.get('TrueLabels') ).shape[0]*0.7) ]
            B[:c,i]=Ebenen.get(layer)[ np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7) : ]
            #print( B.shape)
        elif ('TIF_n' in layer) or ('TrueLabels' in layer):  
            Ebenen[layer]=np.ravel(Ebenen.get(layer))
            #print( layer, Ebenen.get(layer).shape, np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7))
                #,np.min(Ebenen.get(layer)), np.max(Ebenen.get(layer))
            A[:,i]=Ebenen.get(layer)[ : np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7) ]
            B[:c,i]=Ebenen.get(layer)[ np.ceil(np.ravel(Ebenen.get('TrueLabels')).shape[0]*0.7) : ]
        else:
            i-=1
        #    Ebenen[layer]=Mat2Vec(Ebenen.get(layer))
        #    print( layer, Ebenen.get(layer).shape,np.min(Ebenen.get(layer)), np.max(Ebenen.get(layer)))
        #    A[i,:]=Ebenen.get(layer)
        i+=1
        
    #print A.shape
    #A=A.T
    #print A.shape
    return A,B
   
    # Attribute als Zeile, eine Zeile entspricht einem Bild Vektor, nach der Belegung einfach Matrix transponieren 
    #A[1,:] =Layers.get('TIF_r_dem') #TIF_demVec
    #A[2,:] =Layers.get('TIF_r_Slope')
    #A[3,:] =Layers.get('TIF_r_Curvature')
    #A[4,:] =Layers.get('TIF_r_DistStreams')
    #A[5,:] =Layers.get('TIF_r_EucDist_faults')
    ##A[6,:] =Layers.get('TIF_r_EucDist_roads')
    #A[7,:] =Layers.get('TIF_r_EucDist_takhar')
    #A[8,:] =Layers.get('TIF_r_NDVI')
    #A[9,:] =Layers.get('TIF_r_precip')#
    #A[10,:]=Layers.get('TIF_r_B1')
    #A[11,:]=Layers.get('TIF_r_B2')
    #A[12,:]=Layers.get('TIF_r_B3')
    #A[13,:]=Layers.get('TIF_r_B4')
    #A[14,:]=Layers.get('TIF_r_B5')
    #A[15,:]=Layers.get('TIF_r_B6')#
    #A[16,:]=Layers.get('TIF_r_B7')
    #A[17,:]=Layers.get('TIF_r_B8')
    #A[18,:]=Layers.get('TIF_r_B9')
    #A[19,:]=Layers.get('TIF_r_B10')
    #A[20,:]=Layers.get('TIF_r_B11')
    #A[21,:]=Layers.get('TIF_n_ASPN')
    #A[22,:]=Layers.get('TIF_n_ASPE')
    #A[23,:]=Layers.get('TIF_n_ASPS')
    #A[24,:]=Layers.get('TIF_n_ASPW')
    #A[25,:]=Layers.get('TIF_n_LanduseIRA')
    #A[26,:]=Layers.get('TIF_n_LanduseRAL')
    #A[27,:]=Layers.get('TIF_n_LanduseRL')
    #A[28,:]=Layers.get('TIF_n_PLUT')
    #A[29,:]=Layers.get('TIF_n_SEDI')
    #A[30,:]=Layers.get('TIF_n_VOLC')
    #A[31,:]=Layers.get('TrueLabels')

    
def createCheckerboard(Cellsize,Gridsize):
    import numpy as np
    #256x311
    #u = Cellsize     # size eines Feldes
    b = np.zeros(Cellsize**2)
    print( b.shape)
    b.shape = (Cellsize,Cellsize)  #Gridsize x Gridsize Array von nullen
    print( b.shape)
    w = b + 1        #15x15 Array von einsen      
    print( w.shape)
    
    width = Gridsize/(2*Cellsize)     # squares across of a single type
    print( width)
    row1 = np.hstack([w,b]*width)   #(15+15)*20 = 600 spalten a 15 Zeilen
    row2 = np.hstack([b,w]*width)   #  ebenso     600 spalten a 15 Zeilen
    board = np.vstack([row1,row2]*width)  # 600 spalten a 30 Zeilen, 20 mal untereinander packen
    #print( board.shape)
    return board