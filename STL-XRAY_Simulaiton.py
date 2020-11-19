#     import required packages
import os
import gvxrPython3 as gvxr
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
import timeit #to get the time it takes to run the code


start = timeit.default_timer() # start timer to get the duration of the simulation



#       set paths to folders
#           where are the stl files located?
path_to_stl = 'E:/Masterarbeit/Python/MAIN/Creo/STL/'
#           where do you want the xray images to be saved
path_to_xray = 'E:/Masterarbeit/Python/MAIN/bin/'

#       find all files in the stl folder and get all stl-files from it, store them in a list 'stlfiles'
files_in_folder = os.listdir(path_to_stl)
stlfiles=[]
for file in range(len(files_in_folder)):
    if files_in_folder[file][-3:] == 'stl':
        stlfiles.append(files_in_folder[file])
print(str(len(stlfiles))+ 'stl-files found')

#       create openglcontext  
gvxr.createWindow()
gvxr.setWindowSize(512,512)

#       XRay Parameters
#           Source
gvxr.setSourcePosition(0.0,-25.0,0.0,'cm')
gvxr.usePointSource()
gvxr.setMonoChromatic(0.08, 'MeV', 1000)
#           Detector
gvxr.setDetectorPosition(0,10,0,'cm')
gvxr.setDetectorUpVector(0,0,-1)
gvxr.setDetectorNumberOfPixels(128,128)
gvxr.setDetectorPixelSize(0.5,0.5,'mm')


#       create x ray images for all files in the 'stlfiles' - list
for stl in range(len(stlfiles)):        
    #   Load Image
    gvxr.loadMeshFile(stlfiles[stl][:-4], path_to_stl + stlfiles[stl], 'cm')
    print(gvxr.getNumberOfChildren(stlfiles[stl][:-4]))
    #   Set properties of mesh
    label = gvxr.getChildLabel('root', 0)
    
    gvxr.setHU(label,1000) # set houndsfield unit of object
    #   compute the xray image and save it in the chosen folder
    x_ray_image = np.array(gvxr.computeXRayImage())
    np.save(path_to_xray + str(stlfiles[stl][:-4]) + '.npy',x_ray_image)
    np.savetxt(path_to_xray + str(stlfiles[stl][:-4]) + '.txt',x_ray_image)
    #   clear xray cache
    gvxr.removePolygonMeshesFromSceneGraph()
    gvxr.removePolygonMeshesFromXRayRenderer()

    
stop = timeit.default_timer() # stop timer to get the duration of the simulation. 
print('Time: ', stop - start) # print out the duration of the simulation.