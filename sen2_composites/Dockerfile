# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

FROM ubuntu:16.04
MAINTAINER Sebastian Holtkamp <Sebastian.Holtkamp@wwu.de>

# Make workspace and copy all files of current directory into it 
RUN mkdir -p /workspace
WORKDIR /workspace
COPY . /workspace 

# Install dependencies of ndvi.py
RUN apt-get update \
    && apt-get install -qqy --no-install-recommends \
		python-gdal \
        python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install numpy for ndvi.py 
RUN pip3 install numpy

# Run ndvi.py when the container launches
ENTRYPOINT ["python", "sen2_composites.py"]