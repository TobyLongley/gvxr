import os
import gvxrPython3 as gvxr
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import numpy as np


path_to_stl = "E:/Masterarbeit/Python/MAIN/Creo/STL/"
files_in_folder = os.listdir(path_to_stl)
stlfiles=[]
for file in range(len(files_in_folder)):
    if files_in_folder[file][-3:] == "stl":
        stlfiles.append(files_in_folder[file])
print(str(len(stlfiles))+ "stl-files found")


# for stl in range(len(stlfiles)):
for stl in range(4,6):
    #create openglcontext  
    gvxr.createWindow()
    gvxr.setWindowSize(512,512)
    
    #XRay Parameters
    #Source
    gvxr.setSourcePosition(0.0,-25.0,0.0,"cm")
    gvxr.usePointSource()
    gvxr.setMonoChromatic(0.08, "MeV", 1000)
    #Detector
    gvxr.setDetectorPosition(0,10,0,"cm")
    gvxr.setDetectorUpVector(0,0,-1)
    gvxr.setDetectorNumberOfPixels(128,128)
    gvxr.setDetectorPixelSize(0.5,0.5,"mm")
    
    #Load Image
    #gvxr.loadSceneGraph(path_to_stl + stlfiles[stl], 'cm')
    gvxr.loadMeshFile(stlfiles[stl][:-4], path_to_stl + stlfiles[stl], 'cm')
   #print(gvxr.getNumberOfChildren('root'))
    print(gvxr.getNumberOfChildren(stlfiles[stl][:-4]))
    #Set properties of mesh
    label = gvxr.getChildLabel('root', 0)
    
    gvxr.setHU(label,1000) # set houndsfield unit of object

    x_ray_image = np.array(gvxr.computeXRayImage())
    np.save("E:/Masterarbeit/Python/MAIN/X_Ray_Images/" + str(stlfiles[stl][:-4]) + ".npy",x_ray_image)
    np.savetxt("E:/Masterarbeit/Python/MAIN/X_Ray_Images/" + str(stlfiles[stl][:-4]) + ".txt",x_ray_image)
    
    plt.imshow(x_ray_image)
    plt.show()
    #gvxr.renderLoop()
    gvxr.removePolygonMeshesFromSceneGraph()
    gvxr.removePolygonMeshesFromXRayRenderer()
    gvxr.destroyAllWindows()
    

