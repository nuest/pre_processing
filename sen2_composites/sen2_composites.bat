docker build --no-cache -t comp . 
docker run --name=comp_container --mount type=bind,source=%~dp0..\data,target=/workspace/data -e imgfolder=/workspace/data comp
pause
