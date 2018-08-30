
def Spatial_Split_Train_Test(LayerDict):
    
    TestDict=dict()
    TrainDict=dict()
    
    for layer in LayerDict:
        #print layer
        
        TestDict[layer] =LayerDict.get(layer)[:,0:300]
        TrainDict[layer]=LayerDict.get(layer)[:,300:]
        
        
    return (TrainDict, TestDict)