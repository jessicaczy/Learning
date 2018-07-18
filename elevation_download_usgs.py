import arcpy
import numpy
import multiprocessing
import os
import glob
import sys
import time
import logging
from multiprocessing import Process, Queue, Pool, \
  cpu_count, current_process, Manager
import glob
from arcpy import env
from arcpy.sa import *
import random
import urllib
import urllib2, base64
import xlrd


arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("geoprocessing")
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4269)
arcpy.env.scratchWorkspace = "D:/temp_work/sm"
arcpy.env.overwriteOutput = True
arcpy.overwriteOutput = True
arcpy.env.pyramid = "NONE"
arcpy.env.cellSize = "MINOF"
arcpy.env.nodata = "MAXIMUM"
arcpy.env.Workspace = r'D:\FloodiQ-Prod\Regions\Louisiana\Working\raw_elevation'
arcpy.env.compression = "LZW"
arcpy.env.resamplingMethod = "BILINEAR"
workspace = r'D:\FloodiQ-Prod\Regions\Louisiana\Working\raw_elevation'


#start to download
from xlrd import open_workbook
book = open_workbook(r'D:\FloodiQ-Prod\Regions\Louisiana\Working' + os.sep + "download_links.xls")
sheet1 = book.sheet_by_index(0)
files = []
titles =[]

for i in range(1,sheet1.nrows):
    print str(i)

    if i >=0:
        os.chdir(workspace)
        urllib.urlretrieve(sheet1.cell(i,7).value, \
                    filename = sheet1.cell(i,18).value )
####    files.append(sheet1.cell(i,7).value)
####    titles.append(sheet1.cell(i,11).value)
##print titles
##print files

                       

