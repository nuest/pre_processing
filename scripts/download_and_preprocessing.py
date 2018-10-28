# This script imports and runs the functions for downloading, unzipping, atmospheric correction
# and 4-band composite construction
# Takes three input parameters, the working directory in which to store the results
# of the process, the user name and the password for the ESA hub account


from sys import argv
import os
import download_sentinel2
import unzip_sentinel2
import apply_sen2cor
import sen2_composites

wd = argv[1]
user = argv[2]
password = argv[3]


download_sentinel2.download_products(wd, user, password)
unzip_sentinel2.unzip_products(wd)
apply_sen2cor.run_correction(os.path.join(wd, 'sentinel2_files'))
sen2_composites.create_composites(os.path.join(wd, 'sentinel2_files'))