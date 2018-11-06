docker build --no-cache -t composites . 
docker run --name=composites_container --mount type=bind,source=%~dp0..\data,target=/workspace/data -e imgfolder=/workspace/data composites
pause
