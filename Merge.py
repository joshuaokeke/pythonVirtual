import arcpy
import os
import shutil
import re

# Define the paths
input_shapefile = r"C:\pythonVirtual\All_SHAPE_FILES\BATCH_20240713_205316\MTesting071024.shp"
target_gdb = r"C:\pythonVirtual\PA_GIS_DATA\PA GIS MAPPING.gdb"
target_feature_class = os.path.join(target_gdb, "ProjectPoints")

# Check if the target feature class exists
if not arcpy.Exists(target_feature_class):
    print(f"Target feature class {target_feature_class} does not exist.")
else:
    try:
        # Append the shapefile to the feature class
        arcpy.management.Append(inputs=input_shapefile, target=target_feature_class, schema_type="NO_TEST")
        print(f"Successfully merged {input_shapefile} into {target_feature_class}")
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
    except Exception as e:
        print(f"An error occurred: {e}")