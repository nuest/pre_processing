# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

FROM ubuntu:18.04
MAINTAINER Sebastian Holtkamp <Sebastian.Holtkamp@wwu.de>

# Install dependencies 
RUN apt-get update \
    && apt-get install -qqy --no-install-recommends \
		python2.7 \
        python-gdal \
        python-pip \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install numpy 
RUN pip install numpy

# Make workspace and copy all files of current directory into it 
RUN mkdir -p /workspace
WORKDIR /workspace
COPY . /workspace 

# Install Sen2Cor
ENV Sen2Cor_VERSION Sen2Cor-02.05.05-Linux64
RUN mkdir /sen2cor
RUN wget http://step.esa.int/thirdparties/sen2cor/2.5.5/$Sen2Cor_VERSION.run \
    && chmod +x ./$Sen2Cor_VERSION.run \
    && ./$Sen2Cor_VERSION.run \
    && rm ./$Sen2Cor_VERSION.run

ENV PATH "${PATH}:/usr/lib/python2.7"  
ENV PATH "${PATH}:/workspace/Sen2Cor-02.05.05-Linux64/"

# Run sen2_composites.py when the container launches
ENTRYPOINT ["python", "apply_sen2cor.py"]