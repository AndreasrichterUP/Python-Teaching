
def Dict2Blocks(LayerDict) :
    
    # Function get an Input Dictionary and iterates through all layers in the dict
    
    # on each layer the function  - view_as_blocks - cuts the layer in 50x50 Pixel Blocks and saves them in a new
    # dictionary
    
    # the number of blocks is evaluated after the cutting
    # Shapes of the Input layers must have multiple dimensions of 50 otherwise the function will throw an error
    
    # 2 loops iterate though the number of blocks and create a new dictionary for each Block containing all the layers
    # of the Input Data cut to 50x50 Pixels
    
    # The function returns a list of Dictionarys (for each block one) and the Dimension of Blocks horizontal and vertical
    
    from skimage.util.shape import view_as_blocks
    BlocksLayerDict=dict()
    
    
    # schneiden der Ebenen in ein Array of Blocks
    for layer in sorted(LayerDict): 
        LayerBlocks=layer+'_Blocks'
        #print( LayerBlocks)
        
        BlocksLayerDict[LayerBlocks] = view_as_blocks(LayerDict.get(layer), block_shape=(50, 50))
        
    n,m=   BlocksLayerDict.itervalues().next().shape[0:2]
    #print( n,m  )
    BlockList=[]
    for k in range(0,n):
        for l in range(0,m):
            Block='Block_'+str(k)+str(l)
            #print( Block)
            Block=dict()
            
            for layer in sorted(BlocksLayerDict): 
                #print( layer, k, l)
                #print( BlocksLayerDict.get(layer)[k,l].shape)
                Block[layer]=BlocksLayerDict.get(layer)[k,l]
            BlockList.append(Block)

    #BlocksLayerDict  # delete       
    return (BlockList,n,m)


