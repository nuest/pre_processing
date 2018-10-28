set imgfolder=C:\Users\Basti\Desktop\S2A_MSIL1C_20160607T104032_N0202_R008_T32ULC_20160607T104026.SAFE
REM docker build -t sholtkamp/comp . 
docker run --name=comp_container -e imgfolder=%imgfolder% sholtkamp/comp
docker rm comp_container
pause
