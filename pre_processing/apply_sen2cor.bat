docker build  -t apply . 
docker run --name=apply_container --mount type=bind,source=%~dp0..\data,target=/workspace/data -e imgfolder=/workspace/data apply
pause
