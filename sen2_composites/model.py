# Based on the 2016 version written by Daniel Nuest <daniel.nuest@uni-muenster.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import os
import tempfile
import glob
import datetime
from time import gmtime, strftime
from timeit import default_timer as timer

from qgis.core import *
import qgis.utils

print(" ")
print("##### Preparing...")
# Initialize QGIS Application > https://docs.qgis.org/2.8/en/docs/user_manual/processing/console.html
app = QgsApplication([], True)
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()
print("##### QgsApplication initialized.")

# Enable logging
logfilename = os.getenv('QGIS_LOGFILE', os.path.join(tempfile.gettempdir(), 'qgis.log'))
def writelogmessage(message, tag, level):
    with open( logfilename, 'a' ) as logfile:
        logfile.write( '{}({}): {}\n'.format( tag, level, message ) )
QgsMessageLog.instance().messageReceived.connect( writelogmessage )
print("##### QGIS logs to file %s" % logfilename)

print("##### QGIS settings:")
print(QgsApplication.showSettings())

# Import and initialize Processing framework
sys.path.append('/usr/share/qgis/python/plugins')

import warnings; # Silence the error "UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.", see https://github.com/matplotlib/matplotlib/issues/5836#issuecomment-179592427
with warnings.catch_warnings():
    warnings.simplefilter("ignore"); 
    from processing.core.Processing import Processing
    from processing.core.Processing import ProcessingConfig

Processing.initialize()
import processing

# Manually set the OTB path, see https://github.com/qgis/QGIS/blob/master/python/plugins/processing/core/ProcessingConfig.py and https://github.com/qgis/QGIS/blob/master/python/plugins/processing/algs/otb/OTBUtils.py
ProcessingConfig.setSettingValue("OTB_FOLDER", os.getenv('OTB_FOLDER', ''))
ProcessingConfig.setSettingValue("OTB_LIB_FOLDER", os.getenv('OTB_LIB_FOLDER', ''))

print("###### Algorithm help and options:")
processing.alghelp("otb:unsupervisedkmeansimageclassification")
processing.algoptions("otb:unsupervisedkmeansimageclassification")

# Helper function for creating output directory
import errno
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# Get number of classes from envrionment variable within the container
number_of_classes = os.environ['number_of_classes']

# Run qgis based python script, use current timestamp for output directory name
print("###### You chose to calculate " + number_of_classes + " classes")
print("")
input_image = os.path.join(os.environ['QGIS_WORKSPACE'], "odm_orthophoto.tif")
print("###### Input file " + input_image)

output_directory = os.path.join(os.getenv('QGIS_RESULT', os.path.join(tempfile.gettempdir(), 'results')), datetime.datetime.now().strftime("%d.%m.%Y_%H.%M.%S (QGIS " + number_of_classes + " Classes [int])"))
make_sure_path_exists(output_directory)
output_image = os.path.join(output_directory, "Classification.tif")
print("###### Saving output to file to " + output_image)

print("###### Start processing at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " ...")
start = timer()

# Run specific algorithm instead of model using variable number_of_classes
processing.runalg('otb:unsupervisedkmeansimageclassification', input_image, 2048.0, None, 100.0, number_of_classes, 1000.0, 0.0001, output_image, None)

end = timer()
print("###### Processing complete at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ", took " + str(end-start) + " seconds")