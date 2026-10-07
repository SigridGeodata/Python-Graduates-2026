# I am so uploading this to GitHub! 

# Importer biblioteker 
import arcpy, os, sys
import time 
import pandas as pd
import numpy as np

start_time1 = time.time()
def Get_geometry_and_coordiantes(x,y,geometry):
    print(f"X: {x}, Y: {y}, geomerty: {geometry}")

end_time1 = time.time()
Get_geometry_and_coordiantes(4.3,2.6,"Point")
elapsed_time = end_time1 - start_time1
print(f"Time it took to run this function was: {elapsed_time} seconds. Hope you have a good day!") 



start_time2 = time.time()  
def tif_egenskaper(input_tif, message,band_index):
    intermediate_result = arcpy.ia.ExtractBand(input_tif, band_ids=[band_index])
    arr = arcpy.RasterToNumPyArray(intermediate_result,nodata_to_value=0)

     
    arrSum = arr.sum(1)
    print(arrSum)
    arrSum.shape = (arr.shape[0],1)
    print(arrSum.shape )
    arrPerc = (arr)/arrSum
    print(arrPerc)

    print(message)
end_time2 = time.time()
# pwd_ArcGIS Online = 'SuperSecret_Password' 

# tif_file = # Insert raster file here
tif_egenskaper(input_tif=tif_file,  
    message="Have a grape day!",
    band_index=1)
