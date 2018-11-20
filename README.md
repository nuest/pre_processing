# Pre-processing for Studyproject: „Monitoring conflict areas with satellite image time series“

## Aim:
This container aims to automate the pre-processing of Sentinel-2 data from L1C to L2A.

## Usage:
To use this container run the script apply_sen2cor.bat.

## Required structure:
This container requires a specific folder structure to work:

```bash
.
|---data
|   |---S2B_MSIL1C...
|       |---S2B_MSIL1C[...].SAFE
|
|---pre_processing
|   |---apply_sen2cor.bat
|   |---apply_sen2cor.py
|   |---Dockerfile
|
|---.gitignore
|
|---portainer.bat
|
|---README.md
```          
 
Sentinel-2 data can be aquired at [ESA-Hub](https://scihub.copernicus.eu/dhus/#/home). <br>
Data should look similar to this [example](https://scihub.copernicus.eu/dhus/odata/v1/Products('eff34131-ccbf-4c5e-a3d6-7caa320445d8')/$value)       
