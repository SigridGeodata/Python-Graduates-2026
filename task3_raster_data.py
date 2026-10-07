from osgeo import gdal
import rasterio
import arcpy
import time 

# Suppress gdal warning 
gdal.UseExceptions()

# input_tif=  raster data from download 
def timer_dec(base_fc):
    """This is a decorator for timing functions."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = base_fc(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {end_time-start_time:.2f} \n")
        return results
    return wrapper

@timer_dec
def get_cellsize_rasterio(tif_file:str):
    with rasterio.open(tif_file) as src:
        cell_x, cell_y = src.res

    return print(f"Rasterio cellsize - X: {cell_x:.2f}, Y: {cell_y:.2f}")

@timer_dec
def get_cellsize_gdal(tif_file:str):
    raster = gdal.Open(tif_file)
    gt  = raster.GetGeoTransform()
    cell_x = gt[1]
    cell_y = -gt[5]

    return print(f"Gdal cellsize - X: {cell_x:.2f}, Y: {cell_y:.2f}")

@timer_dec
def get_cellsize_arcpy(tif_file:str):
    ras = arcpy.Raster(tif_file)
    cell_x, cell_y = ras.meanCellWidth, ras.meanCellHeight 

    return print(f"Arcpy cellsize - X: {cell_x:.2f}, Y: {cell_y:.2f}")

if __name__=="__main__":

    get_cellsize_rasterio(input_tif)
    get_cellsize_gdal(input_tif)
    get_cellsize_arcpy(input_tif)
